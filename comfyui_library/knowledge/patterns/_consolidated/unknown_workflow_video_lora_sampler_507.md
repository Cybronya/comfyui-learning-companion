---
name: unknown_workflow_video_lora_sampler_507
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.48025
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1981316750769905665.json, 视频生成/图生视频/2001639345427738626.json, 视频生成/图生视频/1980300907424473089.json, 视频生成/文生视频/1022Alan测-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980811965771763713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_507

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1981316750769905665.json、视频生成/图生视频/2001639345427738626.json、视频生成/图生视频/1980300907424473089.json、视频生成/文生视频/1022Alan测-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980811965771763713.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 3/4 个有
- `WanImageToVideo` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `wanBlockSwap` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `FlashVSRNode` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `SeedVR2GGUF` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 4 | 13% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | normal | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，4 个样本，取值分散，一致性仅 13%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 normal，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
