---
name: unknown_workflow_video_lora_sampler_640
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.845333
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Smooth高质量图生视频极速版_2033413176150204417.json, 视频生成/图生视频/Wan2.2 官改图生视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958522667143950337.json, 视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_640

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Smooth高质量图生视频极速版_2033413176150204417.json、视频生成/图生视频/Wan2.2 官改图生视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958522667143950337.json、视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `JWFloat` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 3 | 80% |
| 采样算法 | 1 | 0 - 1 | 3 | 29% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，3 个样本
- 采样算法 中位数 1，观测区间 0 - 1，3 个样本，取值分散，一致性仅 29%
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
