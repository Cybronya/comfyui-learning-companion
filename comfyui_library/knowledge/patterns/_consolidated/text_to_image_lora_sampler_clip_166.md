---
name: text_to_image_lora_sampler_clip_166
type: Text To Image
frequency: 6
level: strong
coverage: 0.8315
common_nodes: [AudioCrop, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, FlashVSRNode, JjkText, KSampler, LoadAudio, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MultiTextConcatenate, PrimitiveStringMultiline, ProcessString, SaveAudioAdvanced, SaveImage, SimpleMath+, Sleep, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/H3 声音克隆工作流｜上传音频文本即可复刻同款嗓音_2096851493616967681.json, 音频生成/音频生成/H3声音克隆批量版本工作流，音频生成语音克隆批量处理工具_2107972747690332162.json, 音频生成/音频生成/H3声音克隆生成｜音频克隆一键合成高质量语音_2094733831185199106.json, 音频生成/音频生成/H3声音克隆语音复刻｜高保真音频生成制作工具_2096663251756085249.json, 音频生成/音频生成/H3纯声音克隆｜上传音频加文本直接合成音频生成_2088703674741772290.json, 音频生成/音频生成/声音克隆纯音频生成｜H3上传音频内容即可复刻_2089032310741094402.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/H3 声音克隆工作流｜上传音频文本即可复刻同款嗓音_2096851493616967681.json、音频生成/音频生成/H3声音克隆批量版本工作流，音频生成语音克隆批量处理工具_2107972747690332162.json、音频生成/音频生成/H3声音克隆生成｜音频克隆一键合成高质量语音_2094733831185199106.json、音频生成/音频生成/H3声音克隆语音复刻｜高保真音频生成制作工具_2096663251756085249.json、音频生成/音频生成/H3纯声音克隆｜上传音频加文本直接合成音频生成_2088703674741772290.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FlashVSRNode`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MultiTextConcatenate`
- `PrimitiveStringMultiline`
- `ProcessString`
- `SaveAudioAdvanced`
- `SaveImage`
- `SimpleMath+`
- `Sleep`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 5/6 个有
- `CR Prompt List` —— 1/6 个有
- `easy forLoopEnd` —— 1/6 个有
- `easy forLoopStart` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
