---
name: unknown_workflow_lora_sampler_clip_118
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9192
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/动作-左右摇熊舞-超极速图生视频V2_2044137028534669313.json, 视频生成/图生视频/史上最快！Wan2.2高质量图生视频工作流81帧50秒（官方+KJ）_1952381519627259905.json, 视频生成/图生视频/图生视频-自动提示词-最新劲爆模型-（动作片加强）超极速V2_2014030248010059777.json, 视频生成/图生视频/甩胯舞-摇的你心旷神怡-图生视频V3_2042644418431291393.json, 视频生成/图生视频/（动作加强直出切换版）90秒81帧超极速图生视频V2_2003117819518681089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/动作-左右摇熊舞-超极速图生视频V2_2044137028534669313.json、视频生成/图生视频/史上最快！Wan2.2高质量图生视频工作流81帧50秒（官方+KJ）_1952381519627259905.json、视频生成/图生视频/图生视频-自动提示词-最新劲爆模型-（动作片加强）超极速V2_2014030248010059777.json、视频生成/图生视频/甩胯舞-摇的你心旷神怡-图生视频V3_2042644418431291393.json、视频生成/图生视频/（动作加强直出切换版）90秒81帧超极速图生视频V2_2003117819518681089.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 4/5 个有
- `TT_img_enc_v2` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `SimpleMath+` —— 3/5 个有
- `Int` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `ZML_SwitchOutput` —— 1/5 个有
- `ZML_SwitchOutputFive` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `llama_cpp_instruct_adv` —— 1/5 个有
- `llama_cpp_model_loader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 5 | 86% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，5 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
