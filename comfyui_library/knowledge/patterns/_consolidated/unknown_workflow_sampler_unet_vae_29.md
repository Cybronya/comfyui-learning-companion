---
name: unknown_workflow_sampler_unet_vae_29
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.862714
common_nodes: [BatchImagesNode, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline, CR Text, easy imageConcat]
members: [图片生成/图生图/2102196823371898882.json, 图片生成/图生图/2102208875008184321.json, 图片生成/图生图/2102208882394357762.json, 图片生成/图生图/2102221847088685058.json, 图片生成/图生图/2102302751672848386.json, 图片生成/图生图/2102372569633607682.json, 图片生成/图生图/2102379189830770690.json, 图片生成/图生图/2102399015068454914.json, 图片生成/图生图/2102401818163765249.json, 图片生成/图生图/2102556544050225153.json, 图片生成/图生图/2102573736280023041.json, 图片生成/文生图/qwen image2.1多图编辑_2101927769339940865.json, 图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json, 视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_29

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/2102196823371898882.json、图片生成/图生图/2102208875008184321.json、图片生成/图生图/2102208882394357762.json、图片生成/图生图/2102221847088685058.json、图片生成/图生图/2102302751672848386.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
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
- `ComfySwitchNode` —— 12/14 个有
- `ResolutionSelector` —— 12/14 个有
- `JjkText` —— 9/14 个有
- `CR Text` —— 4/14 个有
- `easy showAnything` —— 4/14 个有
- `PreviewAny` —— 3/14 个有
- `SaveImageAdvanced` —— 3/14 个有
- `JDCN_StringToList` —— 2/14 个有
- `Text Multiline` —— 2/14 个有
- `TextCombinerSix` —— 2/14 个有
- `easy imageConcat` —— 2/14 个有
- `EmptyImage` —— 1/14 个有
- `GetImageSize` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `TextInput_` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1920 | 14 | 78% |
| 高度 | 1024 | 1024 - 2560 | 14 | 65% |
| 采样步数 | 50 | 25 - 50 | 14 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1920，14 个样本
- 高度 中位数 1024，观测区间 1024 - 2560，14 个样本
- 采样步数 中位数 50，观测区间 25 - 50，14 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR Text、easy imageConcat
