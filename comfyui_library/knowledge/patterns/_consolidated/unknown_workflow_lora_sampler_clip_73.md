---
name: unknown_workflow_lora_sampler_clip_73
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.865667
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, WanHuMoImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_humo.json, 视频生成/图生视频/52.tonnie-数字人对口型（效果不好）_2007938025782775810.json, 视频生成/图生视频/video_humo_native_unlimited_workflow_1971476193147076609.json, 视频生成/文生视频/HuMo数字人音视频同步-人物唱歌480p_1978263692649357314.json, 视频生成/文生视频/HuMo数字人音视频同步-人物唱歌720p-6秒_1978284951923777537.json, 视频生成/文生视频/HuMo数字人音视频同步-猴子吃桃_1978248140035874818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/video_humo.json、视频生成/图生视频/52.tonnie-数字人对口型（效果不好）_2007938025782775810.json、视频生成/图生视频/video_humo_native_unlimited_workflow_1971476193147076609.json、视频生成/文生视频/HuMo数字人音视频同步-人物唱歌480p_1978263692649357314.json、视频生成/文生视频/HuMo数字人音视频同步-人物唱歌720p-6秒_1978284951923777537.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanHuMoImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `RecordAudio` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `RH_Translator` —— 3/6 个有
- `ContextWindowsManual` —— 2/6 个有
- `VHS_LoadAudioUpload` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | uni_pc | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
