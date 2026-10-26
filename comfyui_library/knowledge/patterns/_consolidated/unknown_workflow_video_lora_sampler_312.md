---
name: unknown_workflow_video_lora_sampler_312
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.482625
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json, 视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json, 视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF-首帧+中间帧+尾帧-图生视频_1988567771254579202.json, 视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF_1987191585169453057.json, 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json, 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_高动态_2014746421920014337.json, 视频生成/图生视频/video_wan2_2_14B_i2v_vbvr-model_2035400286210105346.json, 视频生成/图生视频/video_wan2_2_14B_i2v_vbvr_lora_2034928021357989889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_312

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json、视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json、视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF-首帧+中间帧+尾帧-图生视频_1988567771254579202.json、视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF_1987191585169453057.json、视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 8 个 workflow 都包含：
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
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 6/8 个有
- `WanVideoNAG` —— 6/8 个有
- `INTConstant` —— 5/8 个有
- `WanFirstMiddleLastFrameToVideo` —— 4/8 个有
- `WanImageToVideo` —— 4/8 个有
- `FloatConstant` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `Int` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `WanFirstLastFrameToVideo` —— 1/8 个有
- `easy showAnything` —— 1/8 个有
- `wanBlockSwap` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 75% |
| Prompt 约束强度(CFG) | 7 | 6 - 8 | 8 | 86% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 50% |
| 重绘幅度 | simple | - | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 8，8 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 50%
- 重绘幅度 最常用 simple，8 个样本，一致性 75%
