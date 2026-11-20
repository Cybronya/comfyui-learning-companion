---
name: unknown_workflow_lora_sampler_unet_259
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.893
common_nodes: [CLIPLoader, Int, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键电影自动分镜_1990029677165244418.json, 图片生成/图生图/切换角度qwen_1985569167237689345.json, 平台全量/next-scene-qwen 电影分镜制作_1980145456279883778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_259

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键电影自动分镜_1990029677165244418.json、图片生成/图生图/切换角度qwen_1985569167237689345.json、平台全量/next-scene-qwen 电影分镜制作_1980145456279883778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `ProcessString` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `ShellAgentPluginOutputText` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `CR Prompt List` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `Fast Muter (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1088 | - | 2 | 47% |
| 高度 | 720 | - | 2 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1088，样本不足，未给区间，2 个样本，取值分散，一致性仅 47%
- 高度 中位数 720，样本不足，未给区间，2 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
