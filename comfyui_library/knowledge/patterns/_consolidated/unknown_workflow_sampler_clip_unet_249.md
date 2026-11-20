---
name: unknown_workflow_sampler_clip_unet_249
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9226
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI图片游戏素材风格化_1928268107368775682.json, 图片生成/图生图/Flux-Canny官方工作流_1930179521054457857.json, 图片生成/图生图/Flux-Depth-Lora官方工作流_1930173618850840578.json, 图片生成/图生图/flux图生图控制姿态_1922119460591960065.json, 图片生成/图生图/万物花开流_1915322238680104962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_249

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/AI图片游戏素材风格化_1928268107368775682.json、图片生成/图生图/Flux-Canny官方工作流_1930179521054457857.json、图片生成/图生图/Flux-Depth-Lora官方工作流_1930173618850840578.json、图片生成/图生图/flux图生图控制姿态_1922119460591960065.json、图片生成/图生图/万物花开流_1915322238680104962.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Canny` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `ImageResizeKJ` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `AdjustBrightnessContrastSaturationNode` —— 1/5 个有
- `DepthAnything_V2` —— 1/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 5 | 0% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
