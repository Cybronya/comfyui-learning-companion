---
name: unknown_workflow_lora_sampler_clip_25
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.930182
common_nodes: [BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DetailDaemonSamplerNode, DualCLIPLoader, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApplySimple, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Redux洗图工作流_1955898391345680385.json, 图片生成/图生图/Flux Redux洗图工作流_2020675664122224641.json, 图片生成/图生图/Flux+Redux洗图工作流_1990713474449891329.json, 图片生成/图生图/Flux-Redux洗图工作流_1999806514867171330.json, 图片生成/图生图/Flux_Redux洗图工作流（极致写实小红书风格模仿美少女）_1984262638253260802.json, 图片生成/图生图/Flux_Redux洗图工作流（男人金钱豹）_1984268576913833986.json, 图片生成/图生图/flux redux洗图、风格参考工作流_1965654086169317378.json, 图片生成/图生图/redux洗图工作流_1980567344630120450.json, 图片生成/图生图/电商洗图工作流_1969687604314730498.json, 图片生成/文生图/Flux基础文生图工作流_1997984984822611970.json, 图片生成/文生图/flux洗图工作流_1981983365639356418.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux Redux洗图工作流_1955898391345680385.json、图片生成/图生图/Flux Redux洗图工作流_2020675664122224641.json、图片生成/图生图/Flux+Redux洗图工作流_1990713474449891329.json、图片生成/图生图/Flux-Redux洗图工作流_1999806514867171330.json、图片生成/图生图/Flux_Redux洗图工作流（极致写实小红书风格模仿美少女）_1984262638253260802.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApplySimple`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 10/11 个有
- `CR Text` —— 10/11 个有
- `Image Comparer (rgthree)` —— 10/11 个有
- `JWImageResizeByLongerSide` —— 10/11 个有
- `VAEEncode` —— 10/11 个有
- `Joy_caption_two` —— 9/11 个有
- `Joy_caption_two_load` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `CFGGuider` —— 1/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `EmptyLatentImage` —— 1/11 个有
- `SUPIR_Upscale` —— 1/11 个有
- `easy imageScaleDownToSize` —— 1/11 个有
- `easy imageSize` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 11 | 93% |
| LoRA 文本强度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，11 个样本，取值集中（一致性 93%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
