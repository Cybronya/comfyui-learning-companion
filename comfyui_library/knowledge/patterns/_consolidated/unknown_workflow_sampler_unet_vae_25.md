---
name: unknown_workflow_sampler_unet_vae_25
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.947889
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2509模型，人物多角度分镜图工作流_2048404931266220034.json, 图片生成/图生图/Qwen2511多角度生成_2017774842988204034.json, 图片生成/图生图/Qwen_Edit  场景多角度 短剧场景_2034517083853168642.json, 图片生成/图生图/Qwen_Edit  漫剧场景  多角度  漫剧分镜生成_2034549914549620737.json, 图片生成/图生图/Qwen_Edit_2509多角度（短剧专用）_1998642600527691778.json, 图片生成/图生图/Qwen_Edit_2511   IP角色多视图 多视角 三视图_2039344004965343234.json, 图片生成/图生图/Qwen_Edit_2511 套图  IP角色多视图 多视角 三视图 模特分镜_2042415935906123777.json, 图片生成/图生图/Qwen_Edit_2511多角度角色场景（短剧专用）_2054122507342491650.json, 图片生成/图生图/Qwen_Edit_2511多角度（短剧专用）_2014417657260417025.json, 图片生成/图生图/Qwen_Edit_2511多角度（短剧专用）_2016154463576264705.json, 图片生成/图生图/Qwen_Edit_2511多角度（短剧专用），真的很好用！_2037330464716886017.json, 图片生成/图生图/Qwen_Edit_2511镜头多角度_2017108823558852610.json, 图片生成/图生图/Qwen分镜图生图  多视图  多角度 Qwen_Edit_2511_2067422630306734081.json, 图片生成/图生图/opsv-Qwen_Edit_2511多角度_2080275632545685506.json, 图片生成/图生图/opsv-Qwen_edit2511-场景角色合成3refs_2080279327953997825.json, 图片生成/图生图/opsv-qwen2511-2refs_2080315109892771842.json, 图片生成/图生图/人物一致性多角度分镜直出-制造分镜 Next Scene-v2_2003501812189700097.json, 图片生成/图生图/多角度分镜直出-制造分镜 4.0_1985154261069828098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_25

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2509模型，人物多角度分镜图工作流_2048404931266220034.json、图片生成/图生图/Qwen2511多角度生成_2017774842988204034.json、图片生成/图生图/Qwen_Edit  场景多角度 短剧场景_2034517083853168642.json、图片生成/图生图/Qwen_Edit  漫剧场景  多角度  漫剧分镜生成_2034549914549620737.json、图片生成/图生图/Qwen_Edit_2509多角度（短剧专用）_1998642600527691778.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 16/18 个有
- `GetNode` —— 3/18 个有
- `PreviewImage` —— 3/18 个有
- `SetNode` —— 3/18 个有
- `easy showAnything` —— 3/18 个有
- `RHHiddenNodes` —— 2/18 个有
- `RMBG` —— 2/18 个有
- `Seed (rgthree)` —— 2/18 个有
- `HAIGC_SaveImagesToZip` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 1 - 8 | 18 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 1 - 8，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
