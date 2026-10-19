---
name: text_to_image_lora_sampler_clip_131
type: Text To Image
frequency: 7
level: strong
coverage: 0.836
common_nodes: [AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, EmptyYuE2LatentAudio, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, PreviewAny, SaveAudioAdvanced, SheetSage2AudioToABC, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YuE2GenerateMusic, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2102592380288458754.json, 图片生成/文生图/YuE2音乐生成支持翻唱_音频创作处理工具_2102593981120081922.json, 数字人/数字人/yue2音乐生成工作流，数字人配乐一键出超级好听_2110513129020026882.json, 数字人/数字人/yue2音乐生成工作流，数字人配乐一键出超级好听_2111644237338071041.json, 音频生成/音频生成/YuE2音乐生成ComfyUI音频创作处理工作流_2101030293187686401.json, 音频生成/音频生成/YuE2音乐生成工作流 音频创作处理工具_2099988070207676417.json, 音频生成/音频生成/YuE2音乐生成支持翻唱 音频创作处理工具_2099937977395924993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_131

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/YuE2音乐生成工作流_音频创作处理工具_2102592380288458754.json、图片生成/文生图/YuE2音乐生成支持翻唱_音频创作处理工具_2102593981120081922.json、数字人/数字人/yue2音乐生成工作流，数字人配乐一键出超级好听_2110513129020026882.json、数字人/数字人/yue2音乐生成工作流，数字人配乐一键出超级好听_2111644237338071041.json、音频生成/音频生成/YuE2音乐生成ComfyUI音频创作处理工作流_2101030293187686401.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `EmptyYuE2LatentAudio`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YuE2GenerateMusic`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 6/7 个有
- `Any Switch (rgthree)` —— 5/7 个有
- `VAEDecodeAudioTiled` —— 5/7 个有
- `YuE2GenerateABC` —— 5/7 个有
- `EmptyImage` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `Textbox` —— 3/7 个有
- `TrimAudioDuration` —— 3/7 个有
- `Apply Whisper` —— 2/7 个有
- `Audio Duration` —— 2/7 个有
- `AudioCrop` —— 2/7 个有
- `AudioSeparation` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `easy positive` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
