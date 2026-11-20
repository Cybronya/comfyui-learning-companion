---
name: image_to_image_lora_sampler_unet_80
type: Image To Image
frequency: 7
level: strong
coverage: 0.799571
common_nodes: [CLIPLoader, Int, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/95 mhfjt_2058460332594651137.json, 图片生成/反推提示词/Qwen Next Scene：美女美妆产品广告【分镜生成出图】一致性电影3分镜+ 影视剧情分镜制作_1992399117630459905.json, 图片生成/图生图/(贞贞版)Qwen Edit Next Scene V2模型多镜头分镜制作V1_1980697695679594498.json, 图片生成/图生图/002.Qwen编辑之王023.自动分镜一致性_2034858665345290241.json, 图片生成/图生图/002.Qwen编辑之王025.双主角影视剧情分镜_2034917858714587138.json, 图片生成/图生图/Qwen Edit Next Scene V2模型多镜头分镜制作V1_1980700865378041858.json, 图片生成/图生图/Qwen Edit Next Scene 多镜头分镜制作V1_1979206243426406401.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_80

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/95 mhfjt_2058460332594651137.json、图片生成/反推提示词/Qwen Next Scene：美女美妆产品广告【分镜生成出图】一致性电影3分镜+ 影视剧情分镜制作_1992399117630459905.json、图片生成/图生图/(贞贞版)Qwen Edit Next Scene V2模型多镜头分镜制作V1_1980697695679594498.json、图片生成/图生图/002.Qwen编辑之王023.自动分镜一致性_2034858665345290241.json、图片生成/图生图/002.Qwen编辑之王025.双主角影视剧情分镜_2034917858714587138.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
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
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 6/7 个有
- `RH_LLMAPI_NODE` —— 6/7 个有
- `easy promptLine` —— 6/7 个有
- `CR Prompt Text` —— 3/7 个有
- `Text Concatenate` —— 3/7 个有
- `Anything Everywhere` —— 2/7 个有
- `ShellAgentPluginOutputText` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `CFGNorm` —— 1/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `LayerUtility: TextJoin` —— 1/7 个有
- `ModelSamplingAuraFlow` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | sa_solver | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
