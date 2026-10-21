---
name: unknown_workflow_video_120
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [ConcatTextOfUtils, HunyuanVideoFoley, Images to RGB, RH_Captioner, RH_Translator, VHS_LoadVideo, VHS_SelectImages, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [音频生成/音频生成/HunyuanFoley视频配音_1936704989333196801.json, 音频生成/音频生成/【Work-Fisher】HunyuanFoley自动配音_1962034465210044417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_120

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/HunyuanFoley视频配音_1936704989333196801.json、音频生成/音频生成/【Work-Fisher】HunyuanFoley自动配音_1962034465210044417.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ConcatTextOfUtils`
- `HunyuanVideoFoley`
- `Images to RGB`
- `RH_Captioner`
- `RH_Translator`
- `VHS_LoadVideo`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `SoundFlow_Mixer` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
