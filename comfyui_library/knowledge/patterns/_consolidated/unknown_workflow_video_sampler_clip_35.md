---
name: unknown_workflow_video_sampler_clip_35
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.994
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/万相图生视频_1953415257853186050.json, 图片生成/图生图/首尾帧工作流_2076180255999619073.json, 平台全量/Remix+Qwen3图生视频_1987161123160043521.json, 平台全量/SmoothMix-V2.0首尾多帧视频生成_2017039710929035265.json, 平台全量/SmoothMix首尾帧视频_1979911899015974914.json, 平台全量/Wan2.2-Remix-首尾帧视频_1988211191065526274.json, 视频生成/图生视频/Remix-V2.1-首尾多帧视频生成_2011657248396808193.json, 视频生成/图生视频/Remix-V3.0-首尾多帧视频生成_2033890243190984706.json, 视频生成/图生视频/Remix-V3.0-首尾帧视频_2033895649091002370.json, 视频生成/图生视频/SmoothMix-V2.0首尾帧视频生成_2010689825397018625.json, 视频生成/图生视频/WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json, 视频生成/图生视频/WH-AI-Studio-Wan2.2首帧-中间帧-尾帧（加速标准版首中尾帧图生视频）_2022240074083082242.json, 视频生成/图生视频/WH-AI-Studio（短剧必备）指定人物从指定场景出现（图生视频-加速完美版）（人物一致性）_2022215823229718529.json, 视频生成/图生视频/🐳wan2.2 首尾帧 极速臻享版 🦋【官方模型】_1952542983688261634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/万相图生视频_1953415257853186050.json、图片生成/图生图/首尾帧工作流_2076180255999619073.json、平台全量/Remix+Qwen3图生视频_1987161123160043521.json、平台全量/SmoothMix-V2.0首尾多帧视频生成_2017039710929035265.json、平台全量/SmoothMix首尾帧视频_1979911899015974914.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/14 个有
- `ImageResizeKJv2` —— 12/14 个有
- `PathchSageAttentionKJ` —— 11/14 个有
- `CLIPVisionEncode` —— 9/14 个有
- `CLIPVisionLoader` —— 9/14 个有
- `INTConstant` —— 9/14 个有
- `WanFirstLastFrameToVideo` —— 7/14 个有
- `ModelPatchTorchSettings` —— 6/14 个有
- `CR Text` —— 5/14 个有
- `ImpactInt` —— 5/14 个有
- `WanFirstMiddleLastFrameToVideo` —— 5/14 个有
- `WanVideoNAG` —— 4/14 个有
- `ImageResizeKJ` —— 3/14 个有
- `WanImageToVideo` —— 2/14 个有
- `YC Color Match` —— 2/14 个有
- `AILab_QwenVL` —— 1/14 个有
- `GetImageRangeFromBatch` —— 1/14 个有
- `GetImageSizeAndCount` —— 1/14 个有
- `ImageConcanate` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `easy imageRemBg` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 79% |
| Prompt 约束强度(CFG) | 6 | 6 - 35 | 14 | 19% |
| 采样算法 | 1 | 1 - 7.5 | 14 | 0% |
| 调度器 | euler | - | 14 | 79% |
| 重绘幅度 | simple | - | 14 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 79%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 35，14 个样本，取值分散，一致性仅 19%
- 采样算法 中位数 1，观测区间 1 - 7.5，14 个样本，取值分散，一致性仅 0%
- 调度器 最常用 euler，14 个样本，一致性 79%
- 重绘幅度 最常用 simple，14 个样本，一致性 64%
- 风险：Prompt 约束强度(CFG) 观测到 35，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
