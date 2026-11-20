---
name: text_to_image_lora_sampler_clip_149
type: Text To Image
frequency: 11
level: strong
coverage: 0.800636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json, 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json, 图片生成/图生图/Qwen image 2.1图片编辑 局部修改指令式操作_2105111897447157762.json, 图片生成/图生图/Qwen image 2.1多图编辑人物面部加全身三视图角色表V2_2109341094629699586.json, 图片生成/图生图/qwen image2.1多图编辑 换装场景道具一键替换_2104284093109334017.json, 图片生成/图生图/qwen image2.1多图编辑进阶版｜文生图图生图自由切换｜批量改图高效_2102257321794695170.json, 图片生成/图生图/多图编辑qwen image2.1｜场景道具换装 图生图多图协同编辑_2104110886465130498.json, 图片生成/图生图/最强换装工作流，电商服装展示一键换衣图生图处理工具_2106510801598246914.json, 图片生成/文生图/Qwen Image 2.1万能输入工作流，文生图图生图全场景覆盖处理方案_2107588581916233729.json, 图片生成/文生图/Qwen Image 2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2102888298095140865.json, 视频生成/图生视频/Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_149

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json、图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工具_2102505314745667586.json、图片生成/图生图/Qwen image 2.1图片编辑 局部修改指令式操作_2105111897447157762.json、图片生成/图生图/Qwen image 2.1多图编辑人物面部加全身三视图角色表V2_2109341094629699586.json、图片生成/图生图/qwen image2.1多图编辑 换装场景道具一键替换_2104284093109334017.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `BatchImagesNode` —— 9/11 个有
- `easy showAnything` —— 9/11 个有
- `SaveImageAdvanced` —— 8/11 个有
- `ResolutionSelector` —— 7/11 个有
- `ComfySwitchNode` —— 6/11 个有
- `CR Text` —— 5/11 个有
- `GetNode` —— 5/11 个有
- `SetNode` —— 5/11 个有
- `JDCN_StringToList` —— 4/11 个有
- `PreviewAny` —— 4/11 个有
- `Anything Everywhere3` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `easy seed` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `SeedVR2LoadDiTModel` —— 1/11 个有
- `SeedVR2LoadVAEModel` —— 1/11 个有
- `SeedVR2VideoUpscaler` —— 1/11 个有
- `TextInput_` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
