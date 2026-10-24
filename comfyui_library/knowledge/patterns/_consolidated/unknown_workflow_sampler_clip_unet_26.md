---
name: unknown_workflow_sampler_clip_unet_26
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.938625
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/003.FLUX.2智能综合001.lora文生图_2035170208612098050.json, 图片生成/文生图/2031285736095358978.json, 图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json, 图片生成/文生图/EDGE OF QWEN文生图工作流_1957357556198993922.json, 图片生成/文生图/ERNIE 满血版+Turbo版两条工作流，百度大模型_2055111279836180481.json, 图片生成/文生图/ERNIE-Image-Turbo 光影效果 复杂画面处理 光影新世界_2046939542237749250.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图+全节点注释_2046178570917126145.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图-写实风_2045419438635229186.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图V2_2046063492725215234.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2044675520398368770.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2045014051884896258.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2045473705303740418.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2045490522525016066.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2046849642322731009.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2046910510959955970.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2047124098261721089.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2047139433782190082.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2048685419495170049.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2049035575436513282.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图_2052282886828638210.json, 图片生成/文生图/ERNIE-Image-Turbo 文生图生成器_2047546071609511937.json, 图片生成/文生图/ERNIE-Image-Turbo文生图，测试用，感觉效果一般般_2046403986416214017.json, 图片生成/文生图/ERNIE-Image灵韵东方 • 文心一格造像师：定格知识增强的跨模态艺术巅峰_2044349388868292609.json, 图片生成/文生图/自己用小i文生图：Qwen+Lora_2021825579867185154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/003.FLUX.2智能综合001.lora文生图_2035170208612098050.json、图片生成/文生图/2031285736095358978.json、图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json、图片生成/文生图/EDGE OF QWEN文生图工作流_1957357556198993922.json、图片生成/文生图/ERNIE 满血版+Turbo版两条工作流，百度大模型_2055111279836180481.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 22/24 个有
- `EmptyFlux2LatentImage` —— 21/24 个有
- `LoadImage` —— 6/24 个有
- `EmptySD3LatentImage` —— 3/24 个有
- `ModelSamplingAuraFlow` —— 3/24 个有
- `LoraLoader` —— 2/24 个有
- `PreviewImage` —— 2/24 个有
- `RH_LLMAPI_NODE` —— 2/24 个有
- `CR Text` —— 1/24 个有
- `Fast Groups Muter (rgthree)` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | 4 - 50 | 24 | 9% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 24 | 31% |
| 采样算法 | euler | - | 24 | 92% |
| 调度器 | simple | - | 24 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 50，24 个样本，取值分散，一致性仅 9%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，24 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，24 个样本，一致性 92%
- 调度器 最常用 simple，24 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（21/24 个样本）：Steps较低可能导致细节不足
