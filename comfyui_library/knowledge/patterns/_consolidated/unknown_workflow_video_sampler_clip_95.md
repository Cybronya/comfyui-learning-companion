---
name: unknown_workflow_video_sampler_clip_95
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.914143
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频动态加强-PainterI2V_1988236119332536321.json, "视频生成/图生视频/Wan2.2官方ComfyUI图生视频,高质量生成细节把控_1951292355926282242.json", 视频生成/图生视频/wan2.2 首帧图生视频字字1080_2018657772811853825.json, 视频生成/图生视频/wan2.2 首帧图生视频字字720_2018729929084510209.json, 视频生成/图生视频/丝滑SmoothMix模型文图生视频工作流_2036515691074949121.json, 视频生成/图生视频/公路飞行短视频复刻Wan2.2-Smooth+Mix_2004910059593367554.json, 视频生成/图生视频/双图--首尾帧图生视频【2025-11-13】_2010579095784001537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频动态加强-PainterI2V_1988236119332536321.json、视频生成/图生视频/Wan2.2官方ComfyUI图生视频,高质量生成细节把控_1951292355926282242.json、视频生成/图生视频/wan2.2 首帧图生视频字字1080_2018657772811853825.json、视频生成/图生视频/wan2.2 首帧图生视频字字720_2018729929084510209.json、视频生成/图生视频/丝滑SmoothMix模型文图生视频工作流_2036515691074949121.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 6/7 个有
- `CLIPVisionLoader` —— 6/7 个有
- `PathchSageAttentionKJ` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `ImpactInt` —— 5/7 个有
- `ModelPatchTorchSettings` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `Seed (rgthree)` —— 5/7 个有
- `SimpleMath+` —— 5/7 个有
- `WanImageToVideo` —— 5/7 个有
- `Fast Bypasser (rgthree)` —— 2/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/7 个有
- `RIFE VFI` —— 2/7 个有
- `WanFirstLastFrameToVideo` —— 2/7 个有
- `wanBlockSwap` —— 2/7 个有
- `AILab_QwenVL` —— 1/7 个有
- `GetImageSize+` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `PainterI2V` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 57% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 7 | 33% |
| 采样算法 | 1 | 1 - 3.5 | 7 | 36% |
| 调度器 | euler_ancestral | - | 7 | 86% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，7 个样本，取值分散，一致性仅 33%
- 采样算法 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler_ancestral，7 个样本，一致性 86%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
