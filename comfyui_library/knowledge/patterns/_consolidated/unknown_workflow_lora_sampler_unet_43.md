---
name: unknown_workflow_lora_sampler_unet_43
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.907385
common_nodes: [CLIPLoader, CR Prompt Text, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI电商_TVC_短剧 视频续写工具_1990047852929929218.json, 图片生成/图生图/Qwen一图裂变2_1987730592638898178.json, 图片生成/图生图/V5加强一键生成多张分镜自动反推提示_1985349430545162242.json, 图片生成/图生图/[同人同景同服装]超强有一致性模特套图加强版V1（9组）_1985266699085692930.json, 图片生成/图生图/[同人同景同服装]超强有一致性模特套图加强版V2（9组）_1985203219825573890.json, 图片生成/图生图/[同人同景性感写真]一致性加强Qwen-Image-Edit-2511模特套图加速版（10组）_1956097450215964673.json, 图片生成/图生图/[场景变化][多角度版][情境版][同人同服装]超强有一致性模特套图加强版V1（9组）_1987571038110289922.json, 图片生成/图生图/[多角度版][情境版][同人同景同服装]超强有一致性模特套图加强版V1（9组）_1987565150720954370.json, 图片生成/图生图/[多角度版][情境版][同人同景同服装]超强有一致性模特套图加强版V1（9组）_1987932514956324865.json, 图片生成/图生图/一致性套图工作流_1985701504839495682.json, 图片生成/图生图/多视角模特+一致性加强-Qwen_1987023594322636802.json, 平台全量/模特多角度_模特图生成多角度姿势图片_1988782039027552258.json, 视频生成/图生视频/AI电商_TVC_短剧 视频续写工具_1989921636746973185.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_43

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/AI电商_TVC_短剧 视频续写工具_1990047852929929218.json、图片生成/图生图/Qwen一图裂变2_1987730592638898178.json、图片生成/图生图/V5加强一键生成多张分镜自动反推提示_1985349430545162242.json、图片生成/图生图/[同人同景同服装]超强有一致性模特套图加强版V1（9组）_1985266699085692930.json、图片生成/图生图/[同人同景同服装]超强有一致性模特套图加强版V2（9组）_1985203219825573890.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 12/13 个有
- `ProcessString` —— 9/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/13 个有
- `Text Concatenate` —— 6/13 个有
- `easy showAnything` —— 6/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `AILab_QwenVL_Advanced` —— 1/13 个有
- `CR Text` —— 1/13 个有
- `Float` —— 1/13 个有
- `ImpactConditionalBranch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 13 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 92% |
| 调度器 | beta57 | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 92%
- 调度器 最常用 beta57，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
