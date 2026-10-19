---
name: text_to_image_sampler_clip_checkpoint_3
type: Text To Image
frequency: 12
level: strong
coverage: 0.975583
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: [CR Text, easy promptConcat]
members: [sd1.5/lora.png, sd1.5/text-to-image-workflow.png, 图片生成/文生图/1902358353320816641.json, 图片生成/文生图/1904438332934520833.json, 图片生成/文生图/1905913812430819329.json, 图片生成/文生图/1907783762778664961.json, 图片生成/文生图/1908871520008216577.json, 图片生成/文生图/1913538118442778625.json, 图片生成/文生图/1914506513556172801.json, 图片生成/文生图/1916402793215623169.json, 图片生成/文生图/1919010220243357697.json, 图片生成/文生图/1921034287284420610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（sd1.5/lora.png、sd1.5/text-to-image-workflow.png、图片生成/文生图/1902358353320816641.json、图片生成/文生图/1904438332934520833.json、图片生成/文生图/1905913812430819329.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 4/12 个有
- `ArgosTranslateTextNode` —— 1/12 个有
- `CR Text` —— 1/12 个有
- `RH_Prompter` —— 1/12 个有
- `easy promptConcat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 556 | 512 - 1024 | 12 | 75% |
| 高度 | 768 | 512 - 1024 | 12 | 72% |
| LoRA 模型强度 | 0.725 | 0.5 - 1 | 4 | 76% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 20 | 20 - 35 | 12 | 79% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 12 | 97% |
| 采样算法 | dpmpp_2m_sde | - | 12 | 42% |
| 调度器 | karras | - | 12 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 556，观测区间 512 - 1024，12 个样本
- 高度 中位数 768，观测区间 512 - 1024，12 个样本
- LoRA 模型强度 中位数 0.725，观测区间 0.5 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 35，12 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，12 个样本，取值集中（一致性 97%）
- 采样算法 最常用 dpmpp_2m_sde，12 个样本，一致性 42%
- 调度器 最常用 karras，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy promptConcat
