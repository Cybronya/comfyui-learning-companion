---
name: unknown_workflow_sampler_unet_vae
type: Unknown Workflow
frequency: 37
level: strong
coverage: 0.762405
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json, 图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2108369878913740801.json, 图片生成/图生图/image_qwen_image_2.1 角色表_2112852975646494721.json, 图片生成/图生图/qwen-image-1图_2102593163918667778.json, 图片生成/图生图/qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json, 图片生成/图生图/qwen-image-2图_2102599002511462402.json, 图片生成/图生图/qwen-image-3图_2102665111365316610.json, 图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json, 图片生成/图生图/qwen_image_2_1_图像编辑_2101844068895641601.json, 图片生成/图生图/qwen_image_2_1_移除背景_2102572577544818689.json, 图片生成/图生图/一键三视图+多表情+多视角！Qwen Image 2.1！B站艾橘溪_2109323918157897729.json, 图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109583908793835521.json, 图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109608921911611394.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113329806258565121.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113341179273244673.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113348608140599297.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113354096815206402.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113355924818714626.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113362391349161986.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113529216594698242.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113532339434385409.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113533997002346498.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113550242825203714.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113869662944583682.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113870622123192321.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113884432892518401.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113899265037787137.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113923373771350017.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114405604767911938.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114440564266594305.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114585973400100865.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114592092298235906.json, 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114607575722450946.json, 图片生成/图生图/千问Qwen2.1图像编辑_2101904049938452481.json, 图片生成/图生图/多表情+三视图+多视角  Qwen Image 2.1_2114638199283867650.json, 图片生成/图生图/多表情+三视图+多视角  Qwen Image 2.1_2114651292403585026.json, 图片生成/文生图/角色设定集丨Qwen Image 2.1丨多视图·表情·姿态_2112093133474459649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae

> 由 `engine/knowledge_consolidation` 从 37 个 workflow 归纳得出（图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json、图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2108369878913740801.json、图片生成/图生图/image_qwen_image_2.1 角色表_2112852975646494721.json、图片生成/图生图/qwen-image-1图_2102593163918667778.json、图片生成/图生图/qwen-image-2.1：官方原版图生图工作流_2101686169661693953.json…）

- **类型**：Unknown Workflow
- **样本数**：37
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 37 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 36/37 个有
- `ResolutionSelector` —— 33/37 个有
- `ImageStitch` —— 28/37 个有
- `JjkText` —— 28/37 个有
- `PrimitiveFloat` —— 26/37 个有
- `PreviewImage` —— 3/37 个有
- `YK_LoadImageFromURL` —— 3/37 个有
- `ImageScaleToTotalPixels` —— 2/37 个有
- `Text` —— 2/37 个有
- `PrimitiveBoolean` —— 1/37 个有
- `PrimitiveInt` —— 1/37 个有
- `easy promptLine` —— 1/37 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 37 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 37 | 100% |
| 采样算法 | euler | - | 37 | 100% |
| 调度器 | beta | - | 37 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 37 | 100% |
| 宽度 | 1024 | 1024 - 2368 | 37 | 78% |
| 高度 | 1024 | 1024 - 2048 | 37 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，37 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，37 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，37 个样本，一致性 100%
- 调度器 最常用 beta，37 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，37 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2368，37 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，37 个样本
