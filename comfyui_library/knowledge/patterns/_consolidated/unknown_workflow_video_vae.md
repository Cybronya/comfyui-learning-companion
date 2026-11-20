---
name: unknown_workflow_video_vae
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.900857
common_nodes: [HunyuanVideoFoley, SaveLatent, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource]
problems: []
missing: []
members: [平台全量/视频配音 混元-Foley 视频音效 背景音_2013461160678395905.json, 音频生成/音频生成/hunyuan配音_1964226224115564546.json, 音频生成/音频生成/影片配音，音效_2008073310583660545.json, 音频生成/音频生成/影视短剧导演之六：视频音效 背景音_1989874275039498242.json, 音频生成/音频生成/视频配音 混元-Foley 背景音效_1972211822608707586.json, 音频生成/音频生成/视频配音 混元-Foley 视频音效 背景音_1983443250952478721.json, 音频生成/音频生成/视频配音 混元-Foley 视频音效 背景音_1986009915342954497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_vae

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/视频配音 混元-Foley 视频音效 背景音_2013461160678395905.json、音频生成/音频生成/hunyuan配音_1964226224115564546.json、音频生成/音频生成/影片配音，音效_2008073310583660545.json、音频生成/音频生成/影视短剧导演之六：视频音效 背景音_1989874275039498242.json、音频生成/音频生成/视频配音 混元-Foley 背景音效_1972211822608707586.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `HunyuanVideoFoley`
- `SaveLatent`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 6/7 个有
- `LayerUtility: PurgeVRAM V2` —— 5/7 个有
- `AudioCombine` —— 1/7 个有
- `AudioSeparation` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
