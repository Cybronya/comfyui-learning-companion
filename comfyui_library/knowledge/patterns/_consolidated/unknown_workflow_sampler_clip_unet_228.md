---
name: unknown_workflow_sampler_clip_unet_228
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.948833
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/中世纪奇幻女战士_1911987218066669570.json, 图片生成/文生图/云朵精灵Zhiban，三视图_1880497654135418881.json, 图片生成/文生图/在线一键生成毛绒玩具卡通形象手稿丨含效果图_1901132060025856001.json, 图片生成/文生图/大长腿性感女孩生成器可加5个lora 的工作流 FLUX_1964223507485872129.json, 图片生成/文生图/服装设计+模特上身工作流_1981999558349725697.json, 图片生成/文生图/简单logo设计工作流_1981992176706035713.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_228

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/中世纪奇幻女战士_1911987218066669570.json、图片生成/文生图/云朵精灵Zhiban，三视图_1880497654135418881.json、图片生成/文生图/在线一键生成毛绒玩具卡通形象手稿丨含效果图_1901132060025856001.json、图片生成/文生图/大长腿性感女孩生成器可加5个lora 的工作流 FLUX_1964223507485872129.json、图片生成/文生图/服装设计+模特上身工作流_1981999558349725697.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `DetailDaemonSamplerNode` —— 3/6 个有
- `ImageCrop+` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `CR SDXL Aspect Ratio` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `ModelSamplingFlux` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1284 | 512 - 2000 | 6 | 58% |
| 高度 | 1024 | 512 - 1800 | 6 | 65% |
| LoRA 模型强度 | 1 | 0.3 - 1 | 4 | 63% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1284，观测区间 512 - 2000，6 个样本
- 高度 中位数 1024，观测区间 512 - 1800，6 个样本
- LoRA 模型强度 中位数 1，观测区间 0.3 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
