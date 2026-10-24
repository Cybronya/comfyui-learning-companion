---
name: unknown_workflow_lora_sampler_unet_23
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.956778
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit2509多角度分镜直出_1985616988087242754.json, 图片生成/图生图/Qwen Edit2509多角度分镜直出_2002189457388367873.json, 图片生成/图生图/Qwen Image Edit 2511图生图角色多角度版_2053674460150026242.json, 图片生成/图生图/Qwen 三视图 角色多视图 多角度 多视角  Qwen_Edit_2511 图生图_2042105672287916033.json, 图片生成/图生图/Qwen 三视图 角色多视图 多角度 多视角  Qwen_Edit_2511 图生图_2042795583605317634.json, 图片生成/图生图/Qwen 三视图 角色多视图 多角度 多视角  Qwen_Edit_2511 图生图_2042935220361498626.json, 图片生成/图生图/Qwen 图生图 Qwen_Edit_2511 角色多视图 多角度 多视角_2041530373527572482.json, 图片生成/图生图/Qwen 图生图 Qwen_Edit_2511 角色多视图 多角度 多视角_2042104874451603458.json, 图片生成/图生图/Qwen 图生图 Qwen_Edit_2511 角色多视图 多角度 多视角_2042511034333798401.json, 图片生成/图生图/Qwen 图生图 角色多视图 多角度 多视角 Qwen_Edit_2511_2042106304688300033.json, 图片生成/图生图/Qwen-Image-Edit 2511 一图转多视角保持角色一致性（提示词版）_2051930740379668481.json, 图片生成/图生图/Qwen2511多角度生成-URL版_2018176771971096578.json, 图片生成/图生图/Qwen_Edit_2511 角色多视图 多角度 多视角_2037166069290373121.json, 图片生成/图生图/qwen 图生图 IP角色 多视图  多视角  Qwen_Edit_2511_2041716661635522562.json, 图片生成/图生图/一键分镜图生图—多视图+多角度+多视角，可自行调整_2094742222590795777.json, 图片生成/图生图/一键生多图分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2069243753457610754.json, 图片生成/图生图/千问-多角度分镜直出_1996116204152668162.json, 视频生成/图生视频/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2079109724708102146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_23

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Qwen Edit2509多角度分镜直出_1985616988087242754.json、图片生成/图生图/Qwen Edit2509多角度分镜直出_2002189457388367873.json、图片生成/图生图/Qwen Image Edit 2511图生图角色多角度版_2053674460150026242.json、图片生成/图生图/Qwen 三视图 角色多视图 多角度 多视角  Qwen_Edit_2511 图生图_2042105672287916033.json、图片生成/图生图/Qwen 三视图 角色多视图 多角度 多视角  Qwen_Edit_2511 图生图_2042795583605317634.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 16/18 个有
- `Text Multiline` —— 16/18 个有
- `PreviewImage` —— 9/18 个有
- `CR Model Input Switch` —— 2/18 个有
- `PrimitiveStringMultiline` —— 2/18 个有
- `Switch any [Crystools]` —— 2/18 个有
- `CR Text Cycler` —— 1/18 个有
- `ImageURLLoader` —— 1/18 个有
- `UnetLoaderGGUF` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 18 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 94% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，18 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 94%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
