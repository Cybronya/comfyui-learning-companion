---
name: unknown_workflow_controlnet_ipadapter_sampler_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.781333
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, GetImageSize, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, KSamplerAdvanced, LoadImage, PrepImageForClipVision, PreviewImage, SaveImage, VAEDecode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/文生图/场景模仿生成_1940255198012985345.json, 平台全量/一键室外彩色平面图_1892933595080638465.json, 平台全量/景观照片一键景观效果图_1934433841731825666.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/场景模仿生成_1940255198012985345.json、平台全量/一键室外彩色平面图_1892933595080638465.json、平台全量/景观照片一键景观效果图_1934433841731825666.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `KSamplerAdvanced`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `DeepTranslatorTextNode` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `TextInput_` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `PreviewTextNode` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.4 - 0.5 | 3 | 91% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 3 | 100% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | sgm_uniform | - | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.4 - 0.5，3 个样本，取值集中（一致性 91%）
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，3 个样本，一致性 100%
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
