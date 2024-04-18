from transformers import pipeline

#load the text summarization pipeline
 
summarizer = pipeline("summarization")

#function to summarize the text
def summarize_texts(texts, max_length = 3000, min_length= 30):
    summaries = []
    for text in texts:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append({
            'original_text':text,
            'summary': summary[0]['summary_text'],
            'original_length': len(text),
            'summary_length': len(summary[0]['summary_text'])
        })
    return summaries
# test the text summarization function

articles = ["""Moisturizer plays a crucial role in skincare for several reasons. First and foremost, it helps to maintain the skin's hydration levels. Our skin naturally produces oils and lipids that act as a barrier to prevent moisture loss. However, factors such as environmental conditions, harsh cleansers, and aging can compromise this barrier, leading to dryness and dehydration.

Using a moisturizer replenishes the skin's moisture content, helping to restore its natural barrier function. This not only keeps the skin hydrated but also helps to maintain its elasticity and suppleness, reducing the appearance of fine lines and wrinkles over time.

Additionally, moisturizers often contain ingredients that provide other benefits to the skin. For example, they may include antioxidants to protect against environmental damage, vitamins to nourish the skin, or soothing agents to calm irritation and inflammation.

Moreover, keeping the skin well-moisturized can help to prevent various skin issues, such as flakiness, redness, and itching. It can also support the skin's natural healing process, making it more resilient to external aggressors.

In essence, moisturizer is vital because it helps to maintain the health and appearance of the skin by keeping it hydrated, protected, and nourished. Whether you have oily, dry, combination, or sensitive skin, finding the right moisturizer can make a significant difference in your skincare routine.""",
"""Russia is a vast and diverse country, spanning Eastern Europe and Northern Asia, with a rich history, culture, and geopolitical significance. Here's an overview covering various aspects of Russia:

1. **Geography**: Russia is the largest country in the world by land area, covering approximately 17.1 million square kilometers. It spans eleven time zones and has diverse landscapes, including vast plains, mountain ranges like the Ural Mountains and the Caucasus, extensive forests, and Arctic tundra.

2. **History**: Russia has a long and complex history, tracing back to early Slavic tribes, the Kievan Rus', and the medieval Grand Duchy of Moscow. The Russian Empire emerged in the 16th century under the rule of the Tsars, expanding across Eurasia. The Bolshevik Revolution in 1917 led to the establishment of the Soviet Union, which dissolved in 1991, leading to the formation of the Russian Federation.

3. **Culture**: Russian culture is renowned for its contributions to literature, music, dance, and the visual arts. Notable figures include writers like Leo Tolstoy and Fyodor Dostoevsky, composers such as Tchaikovsky and Rachmaninoff, and ballet dancers like Anna Pavlova. Russian cuisine is diverse, with dishes like borscht, pelmeni, and blini being popular.

4. **Economy**: Russia has a mixed economy, with significant natural resources, including oil, natural gas, and minerals. It is one of the world's leading producers and exporters of energy. However, the economy also faces challenges such as corruption, economic sanctions, and dependence on commodity exports.

5. **Politics**: Russia is a federal semi-presidential republic, with the President serving as the head of state and the Prime Minister as the head of government. Vladimir Putin has been a dominant figure in Russian politics, serving as either President or Prime Minister since 1999. The political landscape is characterized by centralized power and limited political pluralism.

6. **International Relations**: Russia plays a significant role in global politics and diplomacy. It is a permanent member of the United Nations Security Council and maintains strategic partnerships with countries across various regions. However, it has also been involved in geopolitical tensions, particularly with Western nations, over issues such as Crimea, Ukraine, and allegations of interference in foreign elections.

7. **Military**: Russia has one of the largest and most advanced militaries in the world, with significant investments in defense technology and capabilities. It maintains a nuclear arsenal and is involved in various military conflicts and peacekeeping operations.

Overall, Russia is a multifaceted country with a complex history, diverse culture, and significant influence on the global stage. Understanding its dynamics requires delving into its rich tapestry of traditions, politics, and society."""
    
]
def summarize_text(text, max_length = 3000, min_length= 30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

summaries = summarize_texts(articles)

#print summaries and statistics for each text
for i, summary in enumerate(summaries):
    print(f"Text {i+1}:\n Original Length: {summary['original_length']} characters\n Summary: {summary['summary']}\nSummary Length: {summary['summary_length']} characters\n")



