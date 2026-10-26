---
name: unknown_workflow_video_lora_sampler_209
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.545
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [数字人/数字人/Wan2.2 I2V FFGO电商视频生成产品介绍_2001583427876974593.json, 视频生成/图生视频/FFGO 多图组合生成动画视频，电影镜头 2025-12-08_1997866783497486337.json, 视频生成/图生视频/Wan2.2快速图生视频_1999450215444869122.json, 视频生成/图生视频/video_wan2_2_14B_i2v_FFGO_basic_workflow_1993579286244294658.json, 视频生成/图生视频/video_wan2_2_14B_i2v_FFGO_change_camera_1993311257635782657.json, 视频生成/图生视频/video_wan2_2_14B_i2v图生视频_1964155751138775041.json, 视频生成/图生视频/三帧流转视频_1996195758498004994.json, 视频生成/图生视频/人物-场景-道具 多图生视频 Wan2_2_14B_i2v_FFGO_basic_2018679573021462530.json, 视频生成/图生视频/超能视频2.0-丐版Wan22-FFGO（参考生视频）_2030310808810430466.json, 视频生成/文生视频/FFGO 多图组合生成动画视频，电影镜头 2025-12-08_2050153435672129537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_209

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/Wan2.2 I2V FFGO电商视频生成产品介绍_2001583427876974593.json、视频生成/图生视频/FFGO 多图组合生成动画视频，电影镜头 2025-12-08_1997866783497486337.json、视频生成/图生视频/Wan2.2快速图生视频_1999450215444869122.json、视频生成/图生视频/video_wan2_2_14B_i2v_FFGO_basic_workflow_1993579286244294658.json、视频生成/图生视频/video_wan2_2_14B_i2v_FFGO_change_camera_1993311257635782657.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 10 个 workflow 都包含：
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
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 9/10 个有
- `INTConstant` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `ImageStitch` —— 8/10 个有
- `PainterI2V` —— 8/10 个有
- `RMBG` —— 8/10 个有
- `TrimVideoLatent` —— 8/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `RIFE VFI` —— 2/10 个有
- `WanImageToVideo` —— 2/10 个有
- `AILab_ImageStitch` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `CR SDXL Aspect Ratio` —— 1/10 个有
- `ImageRotate` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy promptConcat` —— 1/10 个有
- `llama_cpp_instruct_adv` —— 1/10 个有
- `llama_cpp_model_loader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 90% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 10 | 85% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | lcm | - | 10 | 90% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 90%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，10 个样本，取值集中（一致性 85%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，10 个样本，一致性 90%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
