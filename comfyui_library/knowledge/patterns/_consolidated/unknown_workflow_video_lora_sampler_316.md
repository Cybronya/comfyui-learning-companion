---
name: unknown_workflow_video_lora_sampler_316
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.49225
common_nodes: [AILab_QwenVL, CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1987760541282316290.json, 视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1995688996271435777.json, 视频生成/图生视频/video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_1991421095259631618.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_1994587413886476290.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_sfw_2012485583641255937.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_sfw_2013095948842438657.json, 视频生成/图生视频/首尾帧视频_2005138908902031361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_316

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1987760541282316290.json、视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1995688996271435777.json、视频生成/图生视频/video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json、视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_1991421095259631618.json、视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_1994587413886476290.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 8 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 6/8 个有
- `DuckHideNode` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `LayerUtility: PurgeVRAM V2` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `easy saveText` —— 5/8 个有
- `ColorMatch` —— 4/8 个有
- `PainterI2V` —— 4/8 个有
- `WanFirstLastFrameToVideo` —— 4/8 个有
- `RunningHub Deepcleaner` —— 3/8 个有
- `Textbox` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `Int` —— 2/8 个有
- `MultiLinePromptMG` —— 2/8 个有
- `TT_img_enc_v2` —— 2/8 个有
- `Text Multiline` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 62% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | lcm | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
