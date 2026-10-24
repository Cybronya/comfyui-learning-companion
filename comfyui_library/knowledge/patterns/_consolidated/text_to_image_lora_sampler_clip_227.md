---
name: text_to_image_lora_sampler_clip_227
type: Text To Image
frequency: 8
level: strong
coverage: 0.812
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ComfySwitchNode, EmptyLatentImage, InvertMask, JjkText, KSampler, LoadBackgroundRemovalModel, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, RemoveBackground, SaveImage, TextEncodeQwenImage21, TripoSplatConditioning, TripoSplatPreprocessImage, UNETLoader, VAEDecode, VAEDecodeTripoSplat, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1 Triposplat+AnyAngles-T｜角色任意角度图像生成_2108391517315485697.json, 图片生成/图生图/Qwen2.1 Triposplat加AnyAngles T角色任意角度图像生成工作流_2108622833558581250.json, 图片生成/图生图/Qwen2.1 Triposplat加AnyAngles-T，角色任意角度分镜出图_2111898485028118529.json, 图片生成/图生图/Qwen2.1加Triposplat AnyAngles-T｜角色任意角度出图_2111146451723177985.json, 图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json, 图片生成/文生图/Qwen Image 2.1图生图任意角度转换，多视角图生图处理工具_2105738982297522178.json, 图片生成/文生图/任意角度转换加载3d版｜Qwen Image2.1 图生图多视角更精准_2105543517916450818.json, 图片生成/文生图/图生图任意角度转换｜Qwen Image2.1 多角度视图一键生成_2105565075879845889.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_227

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen2.1 Triposplat+AnyAngles-T｜角色任意角度图像生成_2108391517315485697.json、图片生成/图生图/Qwen2.1 Triposplat加AnyAngles T角色任意角度图像生成工作流_2108622833558581250.json、图片生成/图生图/Qwen2.1 Triposplat加AnyAngles-T，角色任意角度分镜出图_2111898485028118529.json、图片生成/图生图/Qwen2.1加Triposplat AnyAngles-T｜角色任意角度出图_2111146451723177985.json、图片生成/文生图/Qwen Image 2.1图生图任意角度转换加载3D版，图生图多视角处理工具_2105729449948966913.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `InvertMask`
- `JjkText`
- `KSampler`
- `LoadBackgroundRemovalModel`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `RemoveBackground`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TripoSplatConditioning`
- `TripoSplatPreprocessImage`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTripoSplat`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateCameraInfo` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `SplatToFile3D` —— 6/8 个有
- `GetNode` —— 4/8 个有
- `JoinImageWithAlpha` —— 4/8 个有
- `PreviewGaussianSplat` —— 4/8 个有
- `RenderMesh` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `SplatToMesh` —— 4/8 个有
- `TripoSplatSamplingPreview` —— 4/8 个有
- `ImageConcanate` —— 2/8 个有
- `ImageScaleToMaxDimension` —— 2/8 个有
- `Load3D` —— 2/8 个有
- `RenderSplat` —— 2/8 个有
- `SaveGLB` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
