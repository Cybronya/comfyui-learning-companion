---
name: unknown_workflow_video_lora_sampler_497
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5724
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2+SVI2 PRO 剧本式长视频自动流 (Auto-Storyteller)_2006374874046009346.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_final_2006035355308400642.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_smoothremix_2008049171638521858.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_generate_extend_once_2005949254709506050.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_video_extend_2005944550638186497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_497

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2+SVI2 PRO 剧本式长视频自动流 (Auto-Storyteller)_2006374874046009346.json、视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_final_2006035355308400642.json、视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_auto_extend2_smoothremix_2008049171638521858.json、视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_generate_extend_once_2005949254709506050.json、视频生成/图生视频/video_wan2_2_14B_i2v_svi_pro_video_extend_2005944550638186497.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `easy forLoopEnd` —— 3/5 个有
- `easy forLoopStart` —— 3/5 个有
- `easy promptLine` —— 3/5 个有
- `PreviewAny` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `DF_Int_to_Float` —— 1/5 个有
- `GODMT_ListGetByIndex` —— 1/5 个有
- `GODMT_SplitString` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `StringToInt` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `WWAA-LineCount` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 5 | 88% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 80% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，5 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 80%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
