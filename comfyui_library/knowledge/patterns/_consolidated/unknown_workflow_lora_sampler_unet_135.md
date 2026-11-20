---
name: unknown_workflow_lora_sampler_unet_135
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.920333
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, UNETLoader, VAEDecode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/分镜剧照洗图+帧境衔接+人物多角度+分镜场景视角生成+Qwen+edit+空间光影质感重绘_2068855572929273858.json, 图片生成/图生图/分镜剧照洗图+帧境衔接+人物多角度+分镜场景视角生成+Qwen+edit+空间光影质感重绘_2077289226323972097.json, 图片生成/图生图/分镜图生成_2116004429735485442.json, 图片生成/图生图/分镜图生成（人物）_2116064057198465026.json, 图片生成/文生图/分镜剧照洗图 帧境衔接 人物多角度 分镜场景视角生成 Qwen edit 空间光影质感重绘_2066884811427508226.json, 平台全量/分镜剧照洗图 帧境衔接 人物多角度 分镜场景视角生成 Qwen edit 空间光影质感重绘_2066694025385697282.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_135

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/分镜剧照洗图+帧境衔接+人物多角度+分镜场景视角生成+Qwen+edit+空间光影质感重绘_2068855572929273858.json、图片生成/图生图/分镜剧照洗图+帧境衔接+人物多角度+分镜场景视角生成+Qwen+edit+空间光影质感重绘_2077289226323972097.json、图片生成/图生图/分镜图生成_2116004429735485442.json、图片生成/图生图/分镜图生成（人物）_2116064057198465026.json、图片生成/文生图/分镜剧照洗图 帧境衔接 人物多角度 分镜场景视角生成 Qwen edit 空间光影质感重绘_2066884811427508226.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `TextEncodeQwenImageEditPlus` —— 5/6 个有
- `CR SDXL Aspect Ratio` —— 4/6 个有
- `RH_Captioner` —— 4/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `CR Prompt Text` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `LayerUtility: TextJoin` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
