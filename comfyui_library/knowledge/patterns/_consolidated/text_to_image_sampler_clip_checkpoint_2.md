---
name: text_to_image_sampler_clip_checkpoint_2
type: Text To Image
frequency: 22
level: moderate
coverage: 0.986682
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: [CR Text, easy promptConcat]
members: [sd1.5/lora.png, sd1.5/text-to-image-workflow.png, 图片生成/文生图/03.混元模型_文生图_1991131442067648514.json, 图片生成/文生图/0728-8_2084094584849780737.json, 图片生成/文生图/0803-2-1_2084239294272729089.json, 图片生成/文生图/0803-2_2084192746373468161.json, 图片生成/文生图/1.文生图基础0609_2064914782632890370.json, 图片生成/文生图/1902358353320816641.json, 图片生成/文生图/1904438332934520833.json, 图片生成/文生图/1905913812430819329.json, 图片生成/文生图/1907783762778664961.json, 图片生成/文生图/1908871520008216577.json, 图片生成/文生图/1913538118442778625.json, 图片生成/文生图/1914506513556172801.json, 图片生成/文生图/1916402793215623169.json, 图片生成/文生图/1919010220243357697.json, 图片生成/文生图/1921034287284420610.json, 图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+lora_2011310284496965634.json, 图片生成/文生图/字体设计_2069831680575238146.json, 图片生成/文生图/御姐_2069833373064982529.json, 图片生成/文生图/手鞠_2106608817659277314.json, 图片生成/文生图/文字_2069832301265113090.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（sd1.5/lora.png、sd1.5/text-to-image-workflow.png、图片生成/文生图/03.混元模型_文生图_1991131442067648514.json、图片生成/文生图/0728-8_2084094584849780737.json、图片生成/文生图/0803-2-1_2084239294272729089.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 9/22 个有
- `ArgosTranslateTextNode` —— 1/22 个有
- `CR Text` —— 1/22 个有
- `RH_Prompter` —— 1/22 个有
- `easy promptConcat` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 660 | 512 - 1288 | 22 | 63% |
| 高度 | 720 | 512 - 1536 | 22 | 63% |
| LoRA 模型强度 | 0.7 | 0.16 - 1 | 9 | 60% |
| LoRA 文本强度 | 0.7 | 0.14 - 1 | 9 | 56% |
| 采样步数 | 20 | 20 - 35 | 22 | 81% |
| Prompt 约束强度(CFG) | 8 | 5 - 8 | 22 | 90% |
| 采样算法 | euler | - | 22 | 45% |
| 调度器 | karras | - | 22 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 660，观测区间 512 - 1288，22 个样本
- 高度 中位数 720，观测区间 512 - 1536，22 个样本
- LoRA 模型强度 中位数 0.7，观测区间 0.16 - 1，9 个样本
- LoRA 文本强度 中位数 0.7，观测区间 0.14 - 1，9 个样本
- 采样步数 中位数 20，观测区间 20 - 35，22 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 8，22 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，22 个样本，一致性 45%
- 调度器 最常用 karras，22 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy promptConcat
