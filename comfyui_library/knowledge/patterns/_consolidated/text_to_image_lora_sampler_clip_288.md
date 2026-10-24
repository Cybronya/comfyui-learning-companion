---
name: text_to_image_lora_sampler_clip_288
type: Text To Image
frequency: 7
level: strong
coverage: 0.839571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveAudioMP3, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/IndexTTS-2.5声音克隆A-16｜情感控制支持五国语言_2107684803452690433.json, 音频生成/音频生成/IndexTTS-2.5声音克隆｜上传参考音频即学即用｜音频生成自然流畅_2102247738854428674.json, 音频生成/音频生成/IndexTTS2.5声音克隆工作流｜语音合成高保真音频生成_2097038903340527618.json, 音频生成/音频生成/IndexTTS2.5语音合成工作流｜声音克隆更稳更拟真_2097218455132008449.json, 音频生成/音频生成/IndexTTS2参考音色克隆｜音频生成拿来做配音神器_2097213028491161601.json, 音频生成/音频生成/上传参考音频文案｜IndexTTS2声音克隆音频生成_2093779915991764994.json, 音频生成/音频生成/声音克隆IndexTTS 2.5情感控制五国语言工作流，音频生成语音克隆工具_2107971183093313538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_288

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（音频生成/音频生成/IndexTTS-2.5声音克隆A-16｜情感控制支持五国语言_2107684803452690433.json、音频生成/音频生成/IndexTTS-2.5声音克隆｜上传参考音频即学即用｜音频生成自然流畅_2102247738854428674.json、音频生成/音频生成/IndexTTS2.5声音克隆工作流｜语音合成高保真音频生成_2097038903340527618.json、音频生成/音频生成/IndexTTS2.5语音合成工作流｜声音克隆更稳更拟真_2097218455132008449.json、音频生成/音频生成/IndexTTS2参考音色克隆｜音频生成拿来做配音神器_2097213028491161601.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_IndexTTS25_Loader` —— 5/7 个有
- `RH_IndexTTS25_Synthesize` —— 5/7 个有
- `AudioCrop` —— 4/7 个有
- `CR Text` —— 4/7 个有
- `Float` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `IndexTTS2BaseNode` —— 1/7 个有
- `IndexTTS2Run` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
