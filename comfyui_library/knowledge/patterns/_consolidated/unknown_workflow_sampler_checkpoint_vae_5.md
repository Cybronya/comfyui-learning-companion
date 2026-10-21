---
name: unknown_workflow_sampler_checkpoint_vae_5
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.729
common_nodes: [AudioEncoderLoader, CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, LoadAudio, PreviewAny, SaveAudioAdvanced, SheetSage2AudioToABC, VAEDecodeAudio, VAEDecodeAudioTiled, YuE2GenerateABC, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [数字人/数字人/yue2超级好听音乐生成工作流_2109992085842653186.json, 音频生成/音频生成/YUE2 comfyui  音乐生成  工作流_2102020803935162369.json, 音频生成/音频生成/YUE2.0 完整版_2099410162128875521.json, 音频生成/音频生成/yue2-音乐生成（支持翻唱）_2099318373120303106.json, 音频生成/音频生成/yue2_comfyui_音乐生成工作流_2099872918548344833.json, 音频生成/音频生成/yue2_comfyui_音频参考修改乐谱版-音乐生成工作流_2100547233820270594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/yue2超级好听音乐生成工作流_2109992085842653186.json、音频生成/音频生成/YUE2 comfyui  音乐生成  工作流_2102020803935162369.json、音频生成/音频生成/YUE2.0 完整版_2099410162128875521.json、音频生成/音频生成/yue2-音乐生成（支持翻唱）_2099318373120303106.json、音频生成/音频生成/yue2_comfyui_音乐生成工作流_2099872918548344833.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderLoader`
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `LoadAudio`
- `PreviewAny`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `VAEDecodeAudio`
- `VAEDecodeAudioTiled`
- `YuE2GenerateABC`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 4/6 个有
- `Textbox` —— 4/6 个有
- `TrimAudioDuration` —— 4/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `1hew_AnySwitchSelect` —— 1/6 个有
- `DF_Text_Box` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 6 | 95% |
| 采样算法 | dpm_2 | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，6 个样本，取值集中（一致性 95%）
- 采样算法 最常用 dpm_2，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
