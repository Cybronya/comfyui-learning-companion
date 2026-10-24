---
name: unknown_workflow_video_lora_sampler_360
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.473
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json, 视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json, 视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF-首帧+中间帧+尾帧-图生视频_1988567771254579202.json, 视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF_1987191585169453057.json, 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json, 视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_高动态_2014746421920014337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_360

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan_2.2_FMLFrame2V 首中尾帧生视频_1988481610276323329.json、视频生成/图生视频/Wan_2.2_FMLF首帧+中帧+尾帧视频工作流_1987819748182396929.json、视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF-首帧+中间帧+尾帧-图生视频_1988567771254579202.json、视频生成/图生视频/video_wan2_2_14B_i2v_Wan22FMLF_1987191585169453057.json、视频生成/图生视频/video_wan2_2_14B_i2v_moremotion_prompt_2011733044515835905.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CFGZeroStar` —— 4/6 个有
- `WanFirstMiddleLastFrameToVideo` —— 4/6 个有
- `WanVideoNAG` —— 4/6 个有
- `INTConstant` —— 3/6 个有
- `FloatConstant` —— 2/6 个有
- `Label (rgthree)` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `WanImageToVideo` —— 2/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `WanFirstLastFrameToVideo` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `wanBlockSwap` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 6 | 87% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 67% |
| 重绘幅度 | simple | - | 6 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，6 个样本，取值集中（一致性 87%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 67%
- 重绘幅度 最常用 simple，6 个样本，一致性 67%
