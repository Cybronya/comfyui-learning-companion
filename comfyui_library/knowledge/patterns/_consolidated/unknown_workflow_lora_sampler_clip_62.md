---
name: unknown_workflow_lora_sampler_clip_62
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.917286
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, WanHuMoImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_humo.json, 数字人/数字人/HuMo数字人原生工作流_1989323404614529026.json, 数字人/数字人/Humo数字人新技术_1968996997191589889.json, 视频生成/图生视频/52.tonnie-数字人对口型（效果不好）_2007938025782775810.json, 视频生成/文生视频/HuMo数字人音视频同步-人物唱歌480p_1978263692649357314.json, 视频生成/文生视频/HuMo数字人音视频同步-人物唱歌720p-6秒_1978284951923777537.json, 视频生成/文生视频/HuMo数字人音视频同步-猴子吃桃_1978248140035874818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/video_humo.json、数字人/数字人/HuMo数字人原生工作流_1989323404614529026.json、数字人/数字人/Humo数字人新技术_1968996997191589889.json、视频生成/图生视频/52.tonnie-数字人对口型（效果不好）_2007938025782775810.json、视频生成/文生视频/HuMo数字人音视频同步-人物唱歌480p_1978263692649357314.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoadAudio` —— 5/7 个有
- `CreateVideo` —— 4/7 个有
- `RecordAudio` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `RH_Translator` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `ContextWindowsManual` —— 2/7 个有
- `VHS_LoadAudioUpload` —— 2/7 个有
- `AudioSeparation` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有
- `SoundFlow_TrimAudio` —— 1/7 个有
- `ToInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 7 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | uni_pc | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，7 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
