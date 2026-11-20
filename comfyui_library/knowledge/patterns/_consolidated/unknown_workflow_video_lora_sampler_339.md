---
name: unknown_workflow_video_lora_sampler_339
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.483556
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json, 视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json, 视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF-首帧+中间帧+尾帧-图生视频_1988567771254579202.json, 视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF_1987191585169453057.json, 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json, 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_高动态_2014746421920014337.json, 视频生成/图生视频/video_wan2_2_14B_i2v_vbvr-model_2035400286210105346.json, 视频生成/图生视频/video_wan2_2_14B_i2v_vbvr_lora_2034928021357989889.json, 视频生成/图生视频/video_wan2_2_with_skill_prompt_2013644132241121282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_339

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json、视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json、视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF-首帧+中间帧+尾帧-图生视频_1988567771254579202.json、视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF_1987191585169453057.json、视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 9 个 workflow 都包含：
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
- `CFGZeroStar` —— 7/9 个有
- `WanVideoNAG` —— 7/9 个有
- `INTConstant` —— 6/9 个有
- `WanImageToVideo` —— 5/9 个有
- `WanFirstMiddleLastFrameToVideo` —— 4/9 个有
- `FloatConstant` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `Int` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `WanFirstLastFrameToVideo` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `wanBlockSwap` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 9 | 86% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | lcm | - | 9 | 56% |
| 重绘幅度 | simple | - | 9 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，9 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，9 个样本，一致性 56%
- 重绘幅度 最常用 simple，9 个样本，一致性 78%
