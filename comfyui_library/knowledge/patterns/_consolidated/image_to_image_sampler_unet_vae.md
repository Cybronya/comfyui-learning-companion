---
name: image_to_image_sampler_unet_vae
type: Image To Image
frequency: 36
level: weak
coverage: 0.880306
common_nodes: [CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen edit 2509 万物白底换背景+反推提示词_1997517208639193089.json, 图片生成/图生图/Qwen-Edit 2511_2046841088454955010.json, 图片生成/图生图/Qwen-Edit-一键生成九宫格表情包_1980174598350213122.json, 图片生成/图生图/Qwen-Edit-人物提取衣服_1965793441999425537.json, 图片生成/图生图/Qwen-Edit-指尖触摸虚拟角色_1983534381887365121.json, 图片生成/图生图/Qwen-Edit-毛绒绒饮料（冬季限定）_1980917424298049537.json, 图片生成/图生图/Qwen-Edit-海的那边是什么_1983545460763893761.json, 图片生成/图生图/Qwen-Edit-生成爆款手办_1964950491358744577.json, 图片生成/图生图/Qwen-Edit-科幻星空眼睛_1984170750527602690.json, 图片生成/图生图/Qwen-Image-Edit ComfyUI 原生工作流_1957867237624610818.json, 图片生成/图生图/Qwen-Image-Edit 真人照片转3D卡通 _ 人物换装_2109096443209404418.json, 图片生成/图生图/Qwen-Image-Edit-4步-手办公仔_1976309393430061057.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步-改变人物视角_1958391993477054466.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步动漫转3D_1958379031286726657.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步女变男_1958389688459542529.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步换文字_1958334945850757121.json, 图片生成/图生图/Qwen-Image-Edit-Lora4步换背景+动作+物品_1958381624465506305.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_1966735948744732674.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2039519268961783810.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2039530385868066818.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2060276950370963458.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2092875395174588417.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2094720617730887681.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2095067512605077506.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2110694065997172737.json, 图片生成/图生图/Qwen-Image-Edit-一键转宫崎骏风_2110697129705566210.json, "图片生成/图生图/Qwen-Image-Edit图像编辑,超强精准控制_1958442372495523841.json", 图片生成/图生图/Qwen-Image-Edit图像编辑丨千问图像编辑_1959825512598286338.json, 图片生成/图生图/Qwen-Image-Edit工作流_1953817263986147329.json, 图片生成/图生图/Qwen一句话改变图片 单图编辑_1991781423713562626.json, 图片生成/图生图/▶Qwen图像编辑流_1958456013403877377.json, 图片生成/图生图/一句话改变图片！图片编辑_1999431845727043586.json, 图片生成/图生图/千问Edit重新打光_1965112456316076033.json, 图片生成/图生图/千问图片修改_2007817860055310337.json, 图片生成/图生图/通义千问2509双图编辑_1985768716262617090.json, 图片生成/图生图/🥯千问Edit 2509版 单图编辑【强化版】🥯_1971749678851289089.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae

> 由 `engine/knowledge_consolidation` 从 36 个 workflow 归纳得出（图片生成/反推提示词/Qwen edit 2509 万物白底换背景+反推提示词_1997517208639193089.json、图片生成/图生图/Qwen-Edit 2511_2046841088454955010.json、图片生成/图生图/Qwen-Edit-一键生成九宫格表情包_1980174598350213122.json、图片生成/图生图/Qwen-Edit-人物提取衣服_1965793441999425537.json、图片生成/图生图/Qwen-Edit-指尖触摸虚拟角色_1983534381887365121.json…）

- **类型**：Image To Image
- **样本数**：36
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 36 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 34/36 个有
- `LoraLoaderModelOnly` —— 34/36 个有
- `ImageScaleToTotalPixels` —— 32/36 个有
- `Image Comparer (rgthree)` —— 25/36 个有
- `CR Text` —— 7/36 个有
- `PreviewImage` —— 6/36 个有
- `Fast Groups Bypasser (rgthree)` —— 4/36 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/36 个有
- `LayerUtility: ImageReel` —— 3/36 个有
- `LayerUtility: ImageReelComposit` —— 3/36 个有
- `TextEncodeQwenImageEditPlus` —— 3/36 个有
- `FluxKontextImageScale` —— 1/36 个有
- `JjkShowText` —— 1/36 个有
- `Note Plus (mtb)` —— 1/36 个有
- `Qwen2.5VL` —— 1/36 个有
- `RH_LLMAPI_NODE` —— 1/36 个有
- `UnetLoaderGGUF` —— 1/36 个有
- `easy cleanGpuUsed` —— 1/36 个有
- `easy promptConcat` —— 1/36 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 36 | 8% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 36 | 50% |
| 采样算法 | euler | - | 36 | 100% |
| 调度器 | simple | - | 36 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 36 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/36 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，36 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，36 个样本
- 采样算法 最常用 euler，36 个样本，一致性 100%
- 调度器 最常用 simple，36 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，36 个样本，取值集中（一致性 93%）
- 高发问题（30/36 个样本）：Steps较低可能导致细节不足
