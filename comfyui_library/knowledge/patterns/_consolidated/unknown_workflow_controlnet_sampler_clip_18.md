---
name: unknown_workflow_controlnet_sampler_clip_18
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.915667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, ImageConcanate, JWImageResizeByLongerSide, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuPulidApply, NunchakuPulidLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Nunchaku超级加速强一致性风格变化线稿控制图生图（吉卜力）_1927603666906419201.json, 图片生成/图生图/nunchaku+pulid+深度控制超级加速工作流_1924820079236554753.json, 图片生成/图生图/nunchaku+pulid+深度控制超级加速工作流_1925363919312068610.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Nunchaku超级加速强一致性风格变化线稿控制图生图（吉卜力）_1927603666906419201.json、图片生成/图生图/nunchaku+pulid+深度控制超级加速工作流_1924820079236554753.json、图片生成/图生图/nunchaku+pulid+深度控制超级加速工作流_1925363919312068610.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuPulidApply`
- `NunchakuPulidLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `AnyLinePreprocessor` —— 1/3 个有
- `BNK_TiledKSampler` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `CropFace` —— 1/3 个有
- `DF_Get_image_size` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FlexLoraLoaderModelOnly` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `PDIMAGE_LongerSize` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Upscale Model Loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.8 | 3 | 86% |
| 采样步数 | 1024 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1024 | - | 1 | 100% |
| 采样算法 | random | - | 1 | 100% |
| 调度器 | 28 | - | 1 | 100% |
| 重绘幅度 | 8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.8，3 个样本，取值集中（一致性 86%）
- 风险：采样步数 观测到 1024，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：Prompt 约束强度(CFG) 观测到 1024，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 8，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
