---
name: unknown_workflow_video_upscale_sampler_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageScale, ImageUpscaleWithModel, Int, LayerUtility: PurgeVRAM, LoadImage, Note Plus (mtb), RIFE VFI, Tiled KSampler, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1901557207723294722.json, 视频生成/图生视频/1901514526544797697.json, 视频生成/图生视频/1901792163662077953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1901557207723294722.json、视频生成/图生视频/1901514526544797697.json、视频生成/图生视频/1901792163662077953.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageScale`
- `ImageUpscaleWithModel`
- `Int`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Note Plus (mtb)`
- `RIFE VFI`
- `Tiled KSampler`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ImageResizeAdvanced` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `ApplyRifleXRoPE_WanVideo` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Lora Loader Stack (rgthree)` —— 1/3 个有
- `TorchCompileModelWanVideo` —— 1/3 个有
- `VRAM_Debug` —— 1/3 个有
- `WanVideoTeaCacheKJ` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 1 | 1 - 1 | 3 | 100% |
| Prompt 约束强度(CFG) | 20 | 15 - 20 | 3 | 87% |
| 采样算法 | 6 | 6 - 6 | 3 | 100% |
| 调度器 | uni_pc | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 20，观测区间 15 - 20，3 个样本，取值集中（一致性 87%）
- 采样算法 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
