---
name: unknown_workflow_sampler_unet_vae_41
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.851333
common_nodes: [BatchImagesNode, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline, CR Text, easy imageConcat]
members: [图片生成/图生图/2102196823371898882.json, 图片生成/图生图/2102208875008184321.json, 图片生成/图生图/2102208882394357762.json, 图片生成/图生图/2102221847088685058.json, 图片生成/图生图/2102302751672848386.json, 图片生成/图生图/2102372569633607682.json, 图片生成/图生图/2102379189830770690.json, 图片生成/图生图/2102399015068454914.json, 图片生成/图生图/2102401818163765249.json, 图片生成/图生图/2102556544050225153.json, 图片生成/图生图/2102573736280023041.json, 视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_41

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2102196823371898882.json、图片生成/图生图/2102208875008184321.json、图片生成/图生图/2102208882394357762.json、图片生成/图生图/2102221847088685058.json、图片生成/图生图/2102302751672848386.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 11/12 个有
- `ResolutionSelector` —— 11/12 个有
- `JjkText` —— 9/12 个有
- `PreviewAny` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `SaveImageAdvanced` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `TextCombinerSix` —— 2/12 个有
- `easy imageConcat` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `EmptyImage` —— 1/12 个有
- `GetImageSize` —— 1/12 个有
- `JDCN_StringToList` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `TextInput_` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1440 | 12 | 89% |
| 高度 | 1024 | 1024 - 2560 | 12 | 63% |
| 采样步数 | 50 | 25 - 50 | 12 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1440，12 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 1024 - 2560，12 个样本
- 采样步数 中位数 50，观测区间 25 - 50，12 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR Text、easy imageConcat
