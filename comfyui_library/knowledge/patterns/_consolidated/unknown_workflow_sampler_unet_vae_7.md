---
name: unknown_workflow_sampler_unet_vae_7
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.84332
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json, 图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表-V2_2108915941747810306.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json, 图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2101994495918297090.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102000830827294721.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2102012967528263682.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2106740180198711298.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2106741898298880001.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2109242621452443649.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2114307543911718914.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图 图生图_2114336682194595842.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图_2102372569633607682.json, 图片生成/图生图/Qwen-Image-2.1 一键扩图！B站艾橘溪_2101946628117721090.json, 图片生成/图生图/Qwen-Image-2.1 图片换头换脸_2102379189830770690.json, 图片生成/图生图/Qwen-Image-2.1 图片换装_2102221847088685058.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2101990292953067522.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102003159496478721.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2102050371035287553.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸_2113474052353519617.json, 图片生成/图生图/Qwen-Image-2.1人物换头+图片换脸！B站艾橘溪_2101851947681800193.json, 图片生成/图生图/Qwen-image2.1  多图像编辑工作流V2_2102399015068454914.json, 图片生成/图生图/qwen image 2.1多图编辑_2101819535304253442.json, 图片生成/文生图/Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102229892883640321.json、图片生成/图生图/Qwen image 2.1图片编辑（配件可用）_2102732245676154881.json、图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表-V2_2108915941747810306.json、图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2105101573423718402.json、图片生成/图生图/Qwen image 2.1多图编辑-人物面部+全身三视图-角色表_2114358796133953538.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
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
- `ResolutionSelector` —— 24/25 个有
- `BatchImagesNode` —— 23/25 个有
- `TextGenerateLTX2Prompt` —— 23/25 个有
- `JjkText` —— 20/25 个有
- `easy showAnything` —— 6/25 个有
- `CR Text` —— 5/25 个有
- `孤海注释` —— 5/25 个有
- `Image Comparer (rgthree)` —— 2/25 个有
- `QwenImage21PromptEnhancerT8` —— 2/25 个有
- `GetImageSize` —— 1/25 个有
- `PreviewAny` —— 1/25 个有
- `easy imageConcat` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 25 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 100% |
| 调度器 | simple | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 25 | 81% |
| 高度 | 1024 | 1024 - 2048 | 25 | 81% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，25 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 100%
- 调度器 最常用 simple，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，25 个样本，取值集中（一致性 81%）
- 高度 中位数 1024，观测区间 1024 - 2048，25 个样本，取值集中（一致性 81%）
