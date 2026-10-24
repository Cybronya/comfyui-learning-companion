---
name: unknown_workflow_video_lora_sampler_125
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.499154
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_14B_i2v_SVI2_2007636774910173185.json, 视频生成/图生视频/Wan2.2快速图生视频_1999450215444869122.json, 视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1987760541282316290.json, 视频生成/图生视频/video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json, 视频生成/图生视频/video_wan2_2_14B_i2v_lightX2V_1030_1983825079475838977.json, 视频生成/图生视频/video_wan2_2_14B_i2v_lightx2v-1030_1984268065183514625.json, 视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_1991421095259631618.json, 视频生成/图生视频/video_wan2_2_14B_i2v_painteri2v_1988481476389945345.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi2-painterI2V_1997917830655934465.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi2_1997912298406731777.json, 视频生成/图生视频/video_wan2_2_14B_i2v_vbvr-model_2035400286210105346.json, 视频生成/图生视频/video_wan2_2_14B_i2v_vbvr_lora_2034928021357989889.json, 视频生成/图生视频/video_wan2_2_14B_i2v图生视频_1964155751138775041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_125

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_14B_i2v_SVI2_2007636774910173185.json、视频生成/图生视频/Wan2.2快速图生视频_1999450215444869122.json、视频生成/图生视频/video_wan2_2_14B_i2v_FLFM2V_optimize_1987760541282316290.json、视频生成/图生视频/video_wan2_2_14B_i2v_FLframe_transition_1986333463185948673.json、视频生成/图生视频/video_wan2_2_14B_i2v_lightX2V_1030_1983825079475838977.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
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
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 9/13 个有
- `PreviewAny` —— 9/13 个有
- `WanImageToVideo` —— 9/13 个有
- `GetImageRangeFromBatch` —— 5/13 个有
- `PainterI2V` —— 3/13 个有
- `FlashVSRNode` —— 2/13 个有
- `WanFirstLastFrameToVideo` —— 2/13 个有
- `CR SDXL Aspect Ratio` —— 1/13 个有
- `ColorMatch` —— 1/13 个有
- `JWStringConcat` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `RH_Translator` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 62% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 13 | 87% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | lcm | - | 13 | 100% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，13 个样本，取值集中（一致性 87%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，13 个样本，一致性 100%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%
