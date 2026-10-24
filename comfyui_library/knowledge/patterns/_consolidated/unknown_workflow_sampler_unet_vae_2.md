---
name: unknown_workflow_sampler_unet_vae_2
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.856
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json, 图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表-V2_2108915941747810306.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2101994495918297090.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102000830827294721.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102012967528263682.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2106740180198711298.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2106741898298880001.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2109242621452443649.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图_2102372569633607682.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图！B站艾橘溪_2101946628117721090.json, 图片生成/图生图/Qwen-Image-2.1 图片换头换脸_2102379189830770690.json, 图片生成/图生图/Qwen-Image-2.1 图片换装_2102221847088685058.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2101990292953067522.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102003159496478721.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102050371035287553.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸！B站艾橘溪_2101851947681800193.json, 图片生成/图生图/Qwen-image2.1  多图像编辑工作流V2_2102399015068454914.json, 图片生成/图生图/qwen image 2.1多图编辑_2101819535304253442.json, 图片生成/图生图/qwen image2.1多图编辑工作流_2112804506063949825.json, 图片生成/图生图/一键扩图！电商必备！超快！_2103068831634771970.json, 图片生成/图生图/图片编辑_qwenimage 2.1_2101829437766586370.json, 图片生成/图生图/多图编辑qwen image2.1_2102573736280023041.json, 图片生成/文生图/qwen image2.1多图编辑_2101927769339940865.json, 图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json, 数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json、图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json、图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表-V2_2108915941747810306.json、图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json、图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2101994495918297090.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 27 个 workflow 都包含：
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
- `BatchImagesNode` —— 25/27 个有
- `TextGenerateLTX2Prompt` —— 25/27 个有
- `ComfySwitchNode` —— 24/27 个有
- `ResolutionSelector` —— 23/27 个有
- `JjkText` —— 17/27 个有
- `easy showAnything` —— 11/27 个有
- `CR Text` —— 8/27 个有
- `SaveImageAdvanced` —— 5/27 个有
- `Image Comparer (rgthree)` —— 3/27 个有
- `JDCN_StringToList` —— 3/27 个有
- `孤海注释` —— 3/27 个有
- `QwenImage21PromptEnhancerT8` —— 2/27 个有
- `PreviewAny` —— 1/27 个有
- `PrimitiveStringMultiline` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 27 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 27 | 100% |
| 采样算法 | euler | - | 27 | 100% |
| 调度器 | simple | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 27 | 76% |
| 高度 | 1024 | 1024 - 2560 | 27 | 63% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，27 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，27 个样本，一致性 100%
- 调度器 最常用 simple，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，27 个样本
- 高度 中位数 1024，观测区间 1024 - 2560，27 个样本
