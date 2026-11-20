---
name: unknown_workflow_sampler_unet_vae_10
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.857286
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json, 图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json, 图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json, 图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2101994495918297090.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102000830827294721.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102012967528263682.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2106740180198711298.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2106741898298880001.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2109242621452443649.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2114307543911718914.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2114336682194595842.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2116857605678260225.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2116865899083948034.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图_2102372569633607682.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图！B站艾橘溪_2101946628117721090.json, 图片生成/图生图/Qwen-Image-2.1 图片换头换脸_2102379189830770690.json, 图片生成/图生图/Qwen-Image-2.1 图片换装_2102221847088685058.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2101990292953067522.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102003159496478721.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102050371035287553.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2113474052353519617.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸！B站艾橘溪_2101851947681800193.json, 图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2105584096473870338.json, 图片生成/图生图/Qwen_image_2.1图片编辑+角色定妆照_2108369878913740801.json, 平台全量/Qwen Image 2.1图片透明分层！ 生成透明图层_2102226349116186626.json, 视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json, 视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json、图片生成/图生图/Qwen-2.1 五视图-透明背景_2103379501370658818.json、图片生成/图生图/Qwen-2.1 图片编辑_2101893576153190401.json、图片生成/图生图/Qwen-2.1多格漫画。_2104722627184128002.json、图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2101994495918297090.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 28 个 workflow 都包含：
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
- `JjkText` —— 26/28 个有
- `ComfySwitchNode` —— 25/28 个有
- `ResolutionSelector` —— 25/28 个有
- `BatchImagesNode` —— 22/28 个有
- `TextGenerateLTX2Prompt` —— 22/28 个有
- `Label (rgthree)` —— 4/28 个有
- `ImageScaleToTotalPixels` —— 3/28 个有
- `ImageStitch` —— 3/28 个有
- `EmptyImage` —— 2/28 个有
- `MultiTextConcatenate` —— 2/28 个有
- `PreviewAny` —— 2/28 个有
- `PreviewImage` —— 2/28 个有
- `Text Multiline` —— 2/28 个有
- `TextCombinerSix` —— 2/28 个有
- `CR Prompt List` —— 1/28 个有
- `GetImageSize` —— 1/28 个有
- `HAIGC_SaveImagesToZip` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 28 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | simple | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |
| 宽度 | 1024 | 1024 - 1536 | 28 | 85% |
| 高度 | 1024 | 1024 - 2048 | 28 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，28 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 simple，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1536，28 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 2048，28 个样本
