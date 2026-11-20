---
name: unknown_workflow_sampler_clip_unet_313
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8958
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QWen-Image中文渲染-文生图+洗图_1953644219829288962.json, 图片生成/文生图/一字马-300张Lora-洗图工作流_1994669431991246850.json, 图片生成/文生图/极致真实的人像质感(Qwen Image 文生图）_1984498747142979586.json, 图片生成/文生图/阿里通义千问Qwen-image文生图+JOY反推【一键】轻松出图_1955074690706542593.json, 平台全量/最强中文模型 - Qwen-Image生图-V1_1953817087259148289.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_313

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/QWen-Image中文渲染-文生图+洗图_1953644219829288962.json、图片生成/文生图/一字马-300张Lora-洗图工作流_1994669431991246850.json、图片生成/文生图/极致真实的人像质感(Qwen Image 文生图）_1984498747142979586.json、图片生成/文生图/阿里通义千问Qwen-image文生图+JOY反推【一键】轻松出图_1955074690706542593.json、平台全量/最强中文模型 - Qwen-Image生图-V1_1953817087259148289.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/5 个有
- `CR SDXL Aspect Ratio` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `QwenImageModelLoader` —— 3/5 个有
- `RH_QwenImageGenerator` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `AILab_QwenVL` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/5 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/5 个有
- `Qwen2.5` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 4 | 5 | 76% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
