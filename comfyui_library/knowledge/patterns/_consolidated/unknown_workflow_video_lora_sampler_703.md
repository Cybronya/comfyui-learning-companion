---
name: unknown_workflow_video_lora_sampler_703
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.565667
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2-LightX2V-图生视频，高速度、超听话（自动提示词）_1981316750769905665.json, 视频生成/图生视频/Wan2.2_Remix（首中尾帧)_2001639345427738626.json, 视频生成/图生视频/wan2.2图生视频_2001269970967330818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_703

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/WAN2.2-LightX2V-图生视频，高速度、超听话（自动提示词）_1981316750769905665.json、视频生成/图生视频/Wan2.2_Remix（首中尾帧)_2001639345427738626.json、视频生成/图生视频/wan2.2图生视频_2001269970967330818.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `FlashVSRNode` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImageLoader` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `SeedVR2GGUF` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `wanBlockSwap` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 3 | 19% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | normal | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，3 个样本，取值分散，一致性仅 19%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 normal，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
