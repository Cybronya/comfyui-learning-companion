---
name: text_to_image_lora_sampler_clip_41
type: Text To Image
frequency: 20
level: strong
coverage: 0.9059
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1单图编辑工作流，风格化图生图单图编辑处理工具_2107594764458745858.json, 图片生成/图生图/Qwen2.1双图组合工作流，风格化图生图双图融合处理工具_2107593203762417666.json, 图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json, 图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2109523834180292610.json, 图片生成/图生图/Qwen2.1透明抠图工作流，图生图抠图背景移除处理工具_2107591647239426050.json, 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json, 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2109524566442856449.json, 图片生成/图生图/Qwen_Image_2.1一键抠图PNG通道输出，透明背景图生图工具_2105110544796708866.json, 图片生成/图生图/Qwen_Image_2.1图像编辑工作流，简洁实用的图生图处理方案_2106169452948709378.json, 图片生成/图生图/Qwen_Image_2.1精准抠图工作流，指哪扣哪的交互式图生图体验_2106553795676303362.json, 图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，图生图快速产出故事板_2105851031333728258.json, 图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，支持三视图参考的图生图工作流_2104738814660014082.json, 图片生成/图生图/qwen-image-2.1一键抠图｜PNG透明通道直出｜抠图发丝级细节保留_2102320037234302977.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2105115732848766978.json, 视频生成/图生视频/Qwen-Image-2.1一键扩图图生图｜写实风格扩展轻松搞定_2107980380883214337.json, 视频生成/图生视频/Qwen_Image_2.1一键图片换装图生图，人物服饰替换处理工具_2104382452906156034.json, 视频生成/图生视频/Qwen_Image_2.1图片换头换脸，一键面部替换的图生图处理工具_2106546399436431361.json, 视频生成/图生视频/Qwen_Image_2.1图片编辑工作流，简洁高效的图生图处理方案_2105520911070875649.json, 视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json, 视频生成/图生视频/qwen_image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2104446242880315393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Qwen2.1单图编辑工作流，风格化图生图单图编辑处理工具_2107594764458745858.json、图片生成/图生图/Qwen2.1双图组合工作流，风格化图生图双图融合处理工具_2107593203762417666.json、图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json、图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2109523834180292610.json、图片生成/图生图/Qwen2.1透明抠图工作流，图生图抠图背景移除处理工具_2107591647239426050.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 15/20 个有
- `PreviewImage` —— 15/20 个有
- `QwenImage21Cache` —— 12/20 个有
- `ComfySwitchNode` —— 10/20 个有
- `ResolutionSelector` —— 9/20 个有
- `BasicGuider` —— 7/20 个有
- `QwenImage21FunPDDLoader` —— 7/20 个有
- `RandomNoise` —— 7/20 个有
- `SamplerCustomAdvanced` —— 7/20 个有
- `SaveImageAdvanced` —— 7/20 个有
- `BatchImagesNode` —— 6/20 个有
- `PrimitiveInt` —— 6/20 个有
- `TextGenerateLTX2Prompt` —— 6/20 个有
- `孤海注释` —— 5/20 个有
- `CR Text` —— 3/20 个有
- `PrimitiveStringMultiline` —— 3/20 个有
- `easy showAnything` —— 3/20 个有
- `GetImageSize` —— 1/20 个有
- `JDCN_StringToList` —— 1/20 个有
- `PrimitiveBoolean` —— 1/20 个有
- `TextInput_` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（21/20 个样本）：Steps较低可能导致细节不足
