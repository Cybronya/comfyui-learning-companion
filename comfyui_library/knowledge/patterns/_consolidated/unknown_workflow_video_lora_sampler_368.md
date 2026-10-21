---
name: unknown_workflow_video_lora_sampler_368
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.544
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1981316750769905665.json, 视频生成/图生视频/2001639345427738626.json, 视频生成/图生视频/1980300907424473089.json, 视频生成/图生视频/1983516962250760194.json, 视频生成/图生视频/2068956549908881410.json, 视频生成/图生视频/1984186286053474306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_368

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1981316750769905665.json、视频生成/图生视频/2001639345427738626.json、视频生成/图生视频/1980300907424473089.json、视频生成/图生视频/1983516962250760194.json、视频生成/图生视频/2068956549908881410.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 6 个 workflow 都包含：
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
- `RIFE VFI` —— 5/6 个有
- `WanImageToVideo` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `wanBlockSwap` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `GetNode` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `FlashVSRNode` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有
- `SeedVR2GGUF` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 50% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 6 | 11% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | normal | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，6 个样本，取值分散，一致性仅 11%
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 normal，6 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
