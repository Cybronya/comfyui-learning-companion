---
name: unknown_workflow_video_lora_sampler_435
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.491
common_nodes: [AILab_QwenVL, CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DuckHideNode, Fast Groups Bypasser (rgthree), GetNode, ImageResizeKJv2, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG, easy saveText]
problems: []
missing: []
members: [视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1995688996271435777.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_1994587413886476290.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_sfw_2012485583641255937.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_sfw_2013095948842438657.json, 视频生成/图生视频/首尾帧视频_2005138908902031361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_435

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1995688996271435777.json、视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_1994587413886476290.json、视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_sfw_2012485583641255937.json、视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_sfw_2013095948842438657.json、视频生成/图生视频/首尾帧视频_2005138908902031361.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DuckHideNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `PainterI2V` —— 3/5 个有
- `RunningHub Deepcleaner` —— 3/5 个有
- `Textbox` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `Int` —— 2/5 个有
- `MultiLinePromptMG` —— 2/5 个有
- `TT_img_enc_v2` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `WanFirstLastFrameToVideo` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
