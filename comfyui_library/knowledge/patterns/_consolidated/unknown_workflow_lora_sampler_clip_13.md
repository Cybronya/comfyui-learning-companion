---
name: unknown_workflow_lora_sampler_clip_13
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.919467
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, KSampler, LoadAudio, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/video_humo.json, 视频生成/图生视频/1978248140035874818.json, 视频生成/图生视频/1978263692649357314.json, 视频生成/图生视频/1978284951923777537.json, 视频生成/图生视频/1977204521292189697.json, 视频生成/图生视频/1960961884411367425.json, 视频生成/文生视频/1961064915547131906.json, 视频生成/文生视频/1961064966939983873.json, 视频生成/文生视频/1961064988674822146.json, 视频生成/文生视频/1978248140035874818.json, 视频生成/文生视频/1978263692649357314.json, 视频生成/文生视频/1978284951923777537.json, 视频生成/文生视频/Wan2.2-S2V对口型-文本+音频+动态参考+控制视频生视频_2072999625805832192.json, 视频生成/文生视频/Wan2.2-S2V对口型-文本+音频+图片+控制视频生视频_2072999626300760064.json, 视频生成/文生视频/Wan2.2-S2V对口型-文本+音频生视频_2072999628041396224.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（comfyui-workflow-templates-json/video_humo.json、视频生成/图生视频/1978248140035874818.json、视频生成/图生视频/1978263692649357314.json、视频生成/图生视频/1978284951923777537.json、视频生成/图生视频/1977204521292189697.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/15 个有
- `VHS_VideoCombine` —— 8/15 个有
- `WanSoundImageToVideo` —— 8/15 个有
- `CreateVideo` —— 7/15 个有
- `RH_Translator` —— 7/15 个有
- `RecordAudio` —— 7/15 个有
- `SaveVideo` —— 7/15 个有
- `WanHuMoImageToVideo` —— 7/15 个有
- `AudioCrop` —— 6/15 个有
- `AudioSeparation` —— 6/15 个有
- `DWPreprocessor` —— 4/15 个有
- `INTConstant` —— 4/15 个有
- `ImageResizeKJv2` —— 4/15 个有
- `VHS_LoadVideo` —— 4/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 15 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | uni_pc | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，15 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
