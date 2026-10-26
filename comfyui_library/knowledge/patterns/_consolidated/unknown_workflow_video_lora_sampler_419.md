---
name: unknown_workflow_video_lora_sampler_419
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.516833
common_nodes: [AILab_QwenVL, CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/Z-video_wan2_2_14B_i2v_lightx2v-1030_1991795364107857922.json, 视频生成/图生视频/video_wan2_2_14B_i2v_lightX2V_1030_1983825079475838977.json, 视频生成/图生视频/video_wan2_2_14B_i2v_lightx2v-1030_1984268065183514625.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi2_1997912298406731777.json, 视频生成/图生视频/图片自动出视频_1989490434684669953.json, 视频生成/图生视频/图生视频千问反推版3_1986291016309362690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_419

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Z-video_wan2_2_14B_i2v_lightx2v-1030_1991795364107857922.json、视频生成/图生视频/video_wan2_2_14B_i2v_lightX2V_1030_1983825079475838977.json、视频生成/图生视频/video_wan2_2_14B_i2v_lightx2v-1030_1984268065183514625.json、视频生成/图生视频/video_wan2_2_14B_i2v_svi2_1997912298406731777.json、视频生成/图生视频/图片自动出视频_1989490434684669953.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 6 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
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
- `WanImageToVideo`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 5/6 个有
- `GetImageRangeFromBatch` —— 5/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageGetSize` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `Switch any [Crystools]` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy textSwitch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | lcm | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
