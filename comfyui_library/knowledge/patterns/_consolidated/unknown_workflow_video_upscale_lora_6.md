---
name: unknown_workflow_video_upscale_lora_6
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.807857
common_nodes: [CLIPLoader, CLIPTextEncode, CM_IntToFloat, ClownsharKSampler_Beta, Display Any (rgthree), GetImageSizeAndCount, ImageFromBatch+, ImageUpscaleWithModelBatched, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/wan2.2 二次放大视频高清修复_1994312405784133634.json, 平台全量/wan2.2视频高清修复_1957373409699229698.json, 平台全量/wan2.2视频高清修复_2040681644251684866.json, 平台全量/视频-最强视频高清修复_1959966424783597570.json, 平台全量/视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2004860711379628033.json, 平台全量/视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2008538185227313153.json, 平台全量/视频画质增强  视频高清放大 wan2.2 视频逐帧修复放大 SeedVR2 2.5 SeedVR2_2008011990899363841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/wan2.2 二次放大视频高清修复_1994312405784133634.json、平台全量/wan2.2视频高清修复_1957373409699229698.json、平台全量/wan2.2视频高清修复_2040681644251684866.json、平台全量/视频-最强视频高清修复_1959966424783597570.json、平台全量/视频放大 Wan2.2-T2V低强度重绘去噪逐帧放大_2004860711379628033.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `ClownsharKSampler_Beta`
- `Display Any (rgthree)`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `ImageUpscaleWithModelBatched`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `VHS_VideoInfoSource` —— 4/7 个有
- `Fast Groups Muter (rgthree)` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `SeedVR2LoadDiTModel` —— 3/7 个有
- `SeedVR2LoadVAEModel` —— 3/7 个有
- `SeedVR2VideoUpscaler` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `VHS_VideoInfo` —— 3/7 个有
- `ImageScale` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | beta57 | - | 7 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 7 | 100% |
| 采样算法 | -1 | -1 - -1 | 7 | 100% |
| 调度器 | 0.2 | 0.2 - 0.53 | 7 | 49% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 beta57，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 0.2，观测区间 0.2 - 0.53，7 个样本，取值分散，一致性仅 49%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 1，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
