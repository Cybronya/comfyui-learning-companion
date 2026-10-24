---
name: text_to_image_lora_sampler_clip_168
type: Text To Image
frequency: 10
level: strong
coverage: 0.8896
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json, 图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json, 图片生成/文生图/Qwen Image 2.1 Viggle 4-Step极速文生图工作流四步出图_2106210534201843714.json, 图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json, 图片生成/文生图/Qwen-Image-2.1-Turbo七步出图｜亚洲人像写真文生图极速版_2111055095529041921.json, 图片生成/文生图/Qwen-Image-2.1-Turbo汉服美学写真｜一键国风服装展示文生图_2111051887217827841.json, 视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json, 视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json, 视频生成/图生视频/Remove模型Qwen_Image_2.1_PE姿势编辑工作流，人物类特效擦除图生图_2108739961490071554.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_168

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json、图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json、图片生成/文生图/Qwen Image 2.1 Viggle 4-Step极速文生图工作流四步出图_2106210534201843714.json、图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json、图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `CR Prompt Text` —— 8/10 个有
- `孤海注释` —— 8/10 个有
- `ComfySwitchNode` —— 7/10 个有
- `QwenPERewriteT8` —— 7/10 个有
- `easy showAnything` —— 6/10 个有
- `PreviewImage` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `Color Grading JK` —— 3/10 个有
- `EmptyImage` —— 3/10 个有
- `LoadImage` —— 3/10 个有
- `PreviewAny` —— 2/10 个有
- `QwenImage21BlockCacheT8` —— 2/10 个有
- `QwenImage21SageAttentionT8` —— 2/10 个有
- `QwenImage21SpectrumT8` —— 2/10 个有
- `AIO_Preprocessor` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `ModelSamplingFlux` —— 1/10 个有
- `QwenPECanvasT8` —— 1/10 个有
- `TextGenerate` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足
