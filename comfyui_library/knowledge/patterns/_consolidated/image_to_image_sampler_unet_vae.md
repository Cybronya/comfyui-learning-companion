---
name: image_to_image_sampler_unet_vae
type: Image To Image
frequency: 30
level: weak
coverage: 0.9042
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2509 基础工作流_1971613466534539266.json, 图片生成/图生图/Qwen-Image-Edit-2511_2004929074399248386.json, 图片生成/图生图/Qwen-Image-Edit-2511新版图像编辑（单图模式工作流）_2011577913421864962.json, 图片生成/图生图/Qwen-Image-Edit-4步-手办公仔_1976309393430061057.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步-改变人物视角_1958391993477054466.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步动漫转3D_1958379031286726657.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步女变男_1958389688459542529.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步换文字_1958334945850757121.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步换背景+动作+物品_1958381624465506305.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_1966735948744732674.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2039519268961783810.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2039530385868066818.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2060276950370963458.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2092875395174588417.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2094720617730887681.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2095067512605077506.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2110694065997172737.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2110697129705566210.json, 图片生成/图生图/Qwen-Image-Edit千问转角度镜头转换_1990070283493101570.json, 图片生成/图生图/Qwen-Image-Edit图像编辑丨千问图像编辑_1959825512598286338.json, 图片生成/图生图/Qwen-Splat_2068695747394105345.json, 图片生成/图生图/Qwen-edit万能一键去水印_2077302903462785026.json, 图片生成/图生图/Qwen2511+模特换装_2003728513553317889.json, 图片生成/图生图/Qwen2511去水印 换装 全能图片V1_2054130825704288257.json, 图片生成/图生图/Qwen2511换装最新图像编辑_2072124811735822338.json, 图片生成/图生图/Qwen2511换装最新图像编辑_2072133881209384962.json, 图片生成/图生图/Qwen_Edit_2511_真正的零偏移工作流_2009132588815880194.json, 图片生成/图生图/apple sharp高斯泼溅成图_2011269417006534657.json, 图片生成/图生图/apple sharp高斯泼溅成图_2025921551727595521.json, 图片生成/图生图/qwen-edit-2509姿势迁移_1982348327364771842.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2509 基础工作流_1971613466534539266.json、图片生成/图生图/Qwen-Image-Edit-2511_2004929074399248386.json、图片生成/图生图/Qwen-Image-Edit-2511新版图像编辑（单图模式工作流）_2011577913421864962.json、图片生成/图生图/Qwen-Image-Edit-4步-手办公仔_1976309393430061057.json、图片生成/图生图/Qwen-Image-Edit-Lora4步-改变人物视角_1958391993477054466.json…）

- **类型**：Image To Image
- **样本数**：30
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 30 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 29/30 个有
- `ImageScaleToTotalPixels` —— 29/30 个有
- `LoraLoaderModelOnly` —— 29/30 个有
- `Image Comparer (rgthree)` —— 16/30 个有
- `TextEncodeQwenImageEdit` —— 16/30 个有
- `TextEncodeQwenImageEditPlus` —— 14/30 个有
- `FluxKontextMultiReferenceLatentMethod` —— 10/30 个有
- `CR Text` —— 6/30 个有
- `PreviewImage` —— 5/30 个有
- `ImageConcanate` —— 4/30 个有
- `PreviewAny` —— 2/30 个有
- `PrimitiveStringMultiline` —— 2/30 个有
- `AIO_Preprocessor` —— 1/30 个有
- `EmptySD3LatentImage` —— 1/30 个有
- `FluxKontextImageScale` —— 1/30 个有
- `JoinStrings` —— 1/30 个有
- `RH_Captioner` —— 1/30 个有
- `RH_Translator` —— 1/30 个有
- `easy imageSize` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 30 | 0% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 4 | 30 | 38% |
| 采样算法 | euler | - | 30 | 97% |
| 调度器 | simple | - | 30 | 97% |
| 重绘幅度 | 1 | 0.85 - 1 | 30 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，30 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 4，30 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，30 个样本，一致性 97%
- 调度器 最常用 simple，30 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，30 个样本，取值集中（一致性 97%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（28/30 个样本）：Steps较低可能导致细节不足
